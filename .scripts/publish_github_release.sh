#!/usr/bin/env bash

REPO="$1"
TAG="$2"
AUTH_TOKEN="$(<'/home/buildbot/.github_token')"

PRERELEASE=true
# declare -a RELEASEFILES=("debs/python-probe_basic_*.deb" "dist/probe_basic-*.tar.gz")
declare -a RELEASEFILES=("dist/probe_basic-*.tar.gz" "pb-installer/bin/ProbeBasic-Installer-*.run")

# commit prefix vs. change log section name
declare -a COMMIT_TYPES=(
"BUG:Bug Fixes"
"ENH:Enhancements and Features"
"API:Braking API changes"
"BLD:Build System"
"TST:Tests System"
"DEP:Deprecated Items"
"DEV:Dev Tools and Utilities"
"DOC:Documentation"
"MNT:Maintenance (refactoring, typos, etc.)"
"STY:Style Fixes (whitespace, PEP8)"
"REL:Release (increment version numbers etc.)"
"SIM:LinuxCNC sim Configs"
"VCP:VCP Examples"
"WIP:Work In Progress"
"REV:Reverted commits"
)

# shellcheck disable=SC2046
LAST_RELEASE=$( git describe --abbrev=0 --tags "$(git rev-list --tags --skip=1  --max-count=1)" )

CREATE_CHANGELOG() {

  # String to accumulate changelog
  CONTENT="Changes since the ${LAST_RELEASE} release.\n\n"

  # Get all commits with type annotations and make them paragraphs.
  for TYPE in "${COMMIT_TYPES[@]}"
    do
      IFS=':' read -r COMMIT_TAG SECTION_TITLE <<< "$TYPE"

      if [ -z "$1" ]
        then
          PARAGRAPH=$(git log --format="* %s (%h)" --grep="^${COMMIT_TAG}")
        else
          PARAGRAPH=$(git log "$1"..HEAD --format="* %s (%h)" --grep="^${COMMIT_TAG}")
      fi
      if [ ! -z "$PARAGRAPH" ]
        then
          PARAGRAPH="${PARAGRAPH//$COMMIT_TAG: /}"
          CONTENT="$CONTENT### $SECTION_TITLE\n\n$PARAGRAPH\n\n"
      fi
    done

  # Regex used to find commits without types
  TYPES_REGEX=""
  for TYPE in "${COMMIT_TYPES[@]}"
    do
      IFS=':' read -r COMMIT_TAG SECTION_TITLE <<< "$TYPE"
      TYPES_REGEX="$TYPES_REGEX$COMMIT_TAG:\|"
  done

  # Get all commit without type annotation and make them another paragraph.
  if [ -z "$1" ]
    then
      PARAGRAPH=$(git log --format=";* %s (%h);")
    else
      PARAGRAPH=$(git log "$1"..HEAD --format=";* %s (%h);")
  fi

  OIFS="$IFS"
  IFS=";"
  FILTERED_PARAGRAPH=""
  for COMMIT in $PARAGRAPH
   do
     TRIMMED_COMMIT="$(echo "$COMMIT" | xargs)"
    if [ ! -z "$TRIMMED_COMMIT" ] && ! echo "$TRIMMED_COMMIT" | grep -q "$TYPES_REGEX"
      then
        FILTERED_PARAGRAPH="$FILTERED_PARAGRAPH$TRIMMED_COMMIT\n"
    fi
  done
  IFS="$OIFS"

  # Only add to content if there are commits without type annotations.
  if [ ! -z "$FILTERED_PARAGRAPH" ]
   then
     CONTENT="$CONTENT### Other\n\n$FILTERED_PARAGRAPH\n\n"
  fi

  # Output changelog
  echo -e "$CONTENT"
}

# -----------------------------------------------------------------------------
# Main script
# =============================================================================

if [ "true" != "$(git rev-parse --is-inside-work-tree 2> /dev/null)" ]
  then
    echo -e "ERROR: This does not seem to be a Git repository"
    exit 1
fi

if [ "$TRAVIS" = "true" ] && [ -z "$TRAVIS_TAG" ]; then
  echo "This build is not for a tag so not creating a release"
  exit 0
fi

TAG_NAME=${TAG:0:7}

echo "Creating GitHub release for $TAG_NAME"

# Generate changelog either from last tag or from beginning of time
if [ -z "$(git tag)" ]
  then
  echo -n "Generating changelog since the begining of time... "
    CONTENT=$(CREATE_CHANGELOG)
  else
  echo -n "Generating changelog since the $LAST_RELEASE release... "
    CONTENT=$(CREATE_CHANGELOG "${LAST_RELEASE}")
fi

echo DONE

FORMAT_CONTENT="$(node -p -e 'JSON.stringify(process.argv[1])' "${CONTENT}")"

echo -n "Creating new draft release... "


JSON=$(cat <<EOF
{
  "tag_name":         "$TAG_NAME",
  "target_commitish": "master",
  "name":             "$TAG_NAME",
  "body":             $FORMAT_CONTENT,
  "draft":            true,
  "prerelease":       $PRERELEASE
}
EOF
)
RESULT=$(curl -s -w "\n%{http_code}\n"     \
  -H "Authorization: token $AUTH_TOKEN"  \
  -d "$JSON"                              \
  "https://api.github.com/repos/$REPO/releases")
if [ "$(echo "$RESULT" | tail -1)" != "201" ]; then
  echo FAILED
  echo "$RESULT"
  exit 1
fi
RELEASEID=$(echo "$RESULT" | sed -ne 's/^  "id": \(.*\),$/\1/p')
if [[ -z "$RELEASEID" ]]; then
  echo FAILED
  echo "$RESULT"
  exit 1
fi
echo DONE

for FILE in "${RELEASEFILES[@]}"; do
  if [ ! -f $FILE ]; then
    echo "Warning: $FILE is not a file"
    continue
  fi
  FILESIZE=$(stat -c '%s' "$FILE")
  # shellcheck disable=SC2006
  FILENAME=`basename "$FILE"`
  echo -n "Uploading $FILENAME... "
  RESULT=$(curl -s -w "\n%{http_code}\n"                   \
    -H "Authorization: token $AUTH_TOKEN"                \
    -H "Accept: application/vnd.github.manifold-preview"  \
    -H "Content-Type: application/zip"                    \
    --data-binary "@$FILE"                                \
    "https://uploads.github.com/repos/$REPO/releases/$RELEASEID/assets?name=$FILENAME&size=$FILESIZE")
  if [ "$(echo "$RESULT" | tail -1)" != "201" ]; then
    echo FAILED
    echo "$RESULT"
    exit 1
  fi
  echo DONE
done

echo -n "Publishing release... "
JSON=$(cat <<EOF
{
  "draft": false
}
EOF
)
RESULT=$(curl -s -w "\n%{http_code}\n"     \
  -X PATCH                                \
  -H "Authorization: token $AUTH_TOKEN"  \
  -d "$JSON"                              \
  "https://api.github.com/repos/$REPO/releases/$RELEASEID")
if [ "$(echo "$RESULT" | tail -1)" = "200" ]; then
  echo DONE
else
  echo FAILED
  echo "$RESULT"
  exit 1
fi
