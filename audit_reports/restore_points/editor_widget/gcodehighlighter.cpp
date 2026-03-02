#include "gcodehighlighter.h"

GCodeHighlighter::GCodeHighlighter(QTextDocument *parent)
	: QSyntaxHighlighter(parent)
	, gCodeHighlightEnabled(true)
	, mCodeHighlightEnabled(true)
	, parameterHighlightEnabled(true)
	, numberHighlightEnabled(true)
	, commentHighlightEnabled(true)
	, stringHighlightEnabled(true)
{
	gCodeFormat.setFontWeight(QFont::Bold);
	mCodeFormat.setFontWeight(QFont::Bold);
	commentFormat.setFontItalic(true);
	applyColors();
}

void GCodeHighlighter::setGCodeHighlightEnabled(bool enabled)
{
	if (gCodeHighlightEnabled == enabled)
		return;
	gCodeHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isGCodeHighlightEnabled() const
{
	return gCodeHighlightEnabled;
}

void GCodeHighlighter::setMCodeHighlightEnabled(bool enabled)
{
	if (mCodeHighlightEnabled == enabled)
		return;
	mCodeHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isMCodeHighlightEnabled() const
{
	return mCodeHighlightEnabled;
}

void GCodeHighlighter::setParameterHighlightEnabled(bool enabled)
{
	if (parameterHighlightEnabled == enabled)
		return;
	parameterHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isParameterHighlightEnabled() const
{
	return parameterHighlightEnabled;
}

void GCodeHighlighter::setNumberHighlightEnabled(bool enabled)
{
	if (numberHighlightEnabled == enabled)
		return;
	numberHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isNumberHighlightEnabled() const
{
	return numberHighlightEnabled;
}

void GCodeHighlighter::setCommentHighlightEnabled(bool enabled)
{
	if (commentHighlightEnabled == enabled)
		return;
	commentHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isCommentHighlightEnabled() const
{
	return commentHighlightEnabled;
}

void GCodeHighlighter::setStringHighlightEnabled(bool enabled)
{
	if (stringHighlightEnabled == enabled)
		return;
	stringHighlightEnabled = enabled;
	rehighlight();
}

bool GCodeHighlighter::isStringHighlightEnabled() const
{
	return stringHighlightEnabled;
}

void GCodeHighlighter::setGCodeColor(const QColor &color)
{
	gCodeFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::gCodeColor() const
{
	return gCodeFormat.foreground().color();
}

void GCodeHighlighter::setMCodeColor(const QColor &color)
{
	mCodeFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::mCodeColor() const
{
	return mCodeFormat.foreground().color();
}

void GCodeHighlighter::setParameterColor(const QColor &color)
{
	parameterFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::parameterColor() const
{
	return parameterFormat.foreground().color();
}

void GCodeHighlighter::setNumberColor(const QColor &color)
{
	numberFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::numberColor() const
{
	return numberFormat.foreground().color();
}

void GCodeHighlighter::setCommentColor(const QColor &color)
{
	commentFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::commentColor() const
{
	return commentFormat.foreground().color();
}

void GCodeHighlighter::setStringColor(const QColor &color)
{
	stringFormat.setForeground(color);
	rehighlight();
}

QColor GCodeHighlighter::stringColor() const
{
	return stringFormat.foreground().color();
}

void GCodeHighlighter::applyColors()
{
	gCodeFormat.setForeground(Qt::darkBlue);
	mCodeFormat.setForeground(Qt::darkMagenta);
	parameterFormat.setForeground(Qt::darkGreen);
	numberFormat.setForeground(Qt::darkRed);
	commentFormat.setForeground(Qt::darkGreen);
	stringFormat.setForeground(Qt::darkCyan);
}

void GCodeHighlighter::highlightBlock(const QString &text)
{
	if (gCodeHighlightEnabled) {
		QRegularExpression gExpression("\\bG[0-9]+(\\.[0-9])?\\b");
		QRegularExpressionMatchIterator gMatches = gExpression.globalMatch(text);
		while (gMatches.hasNext()) {
			QRegularExpressionMatch match = gMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), gCodeFormat);
		}
	}

	if (mCodeHighlightEnabled) {
		QRegularExpression mExpression("\\bM[0-9]+(\\.[0-9])?\\b");
		QRegularExpressionMatchIterator mMatches = mExpression.globalMatch(text);
		while (mMatches.hasNext()) {
			QRegularExpressionMatch match = mMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), mCodeFormat);
		}
	}

	if (parameterHighlightEnabled) {
		QRegularExpression paramExpression("\\b[XYZABCUVWIJKRQPF][+-]?[0-9]+(\\.[0-9]*)?\\b");
		QRegularExpressionMatchIterator paramMatches = paramExpression.globalMatch(text);
		while (paramMatches.hasNext()) {
			QRegularExpressionMatch match = paramMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), parameterFormat);
		}
	}

	if (numberHighlightEnabled) {
		QRegularExpression numberExpression("\\b[0-9]+(\\.[0-9]*)?\\b");
		QRegularExpressionMatchIterator numberMatches = numberExpression.globalMatch(text);
		while (numberMatches.hasNext()) {
			QRegularExpressionMatch match = numberMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), numberFormat);
		}
	}

	if (commentHighlightEnabled) {
		QRegularExpression commentExpression(";[^\\n]*|\\([^\\n]*\\)");
		QRegularExpressionMatchIterator commentMatches = commentExpression.globalMatch(text);
		while (commentMatches.hasNext()) {
			QRegularExpressionMatch match = commentMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), commentFormat);
		}
	}

	if (stringHighlightEnabled) {
		QRegularExpression stringExpression("\"[^\"]*\"|'[^']*'");
		QRegularExpressionMatchIterator stringMatches = stringExpression.globalMatch(text);
		while (stringMatches.hasNext()) {
			QRegularExpressionMatch match = stringMatches.next();
			setFormat(match.capturedStart(), match.capturedLength(), stringFormat);
		}
	}
}
