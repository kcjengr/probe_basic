#!/usr/bin/env bash

# Scan for new debian packages in apt repository

cd /home/buildbot/debian/apt

dpkg-scanpackages --arch amd64 pool/ > dists/develop/main/binary-amd64/Packages
cat dists/develop/main/binary-amd64/Packages | gzip -9 > dists/develop/main/binary-amd64/Packages.gz

cd /home/buildbot/debian/apt/dists/develop

/home/buildbot/debian/generate-release.sh > Release

export GPG_TTY=$(tty)
export GNUPGHOME="/home/buildbot/debian/pgpkeys"

cat /home/buildbot/debian/apt/dists/develop/Release | gpg --default-key 2DEC041F290DF85A -abs > /home/buildbot/debian/apt/dists/develop/Release.gpg
cat /home/buildbot/debian/apt/dists/develop/Release | gpg --default-key 2DEC041F290DF85A -abs --clearsign > /home/buildbot/debian/apt/dists/develop/InRelease

