#ifndef GCODEHIGHLIGHTER_H
#define GCODEHIGHLIGHTER_H

#include <QSyntaxHighlighter>
#include <QRegularExpression>
#include <QColor>

class GCodeHighlighter : public QSyntaxHighlighter
{
	Q_OBJECT

public:
	GCodeHighlighter(QTextDocument *parent = nullptr);

	void setGCodeHighlightEnabled(bool enabled);
	bool isGCodeHighlightEnabled() const;
	void setMCodeHighlightEnabled(bool enabled);
	bool isMCodeHighlightEnabled() const;
	void setParameterHighlightEnabled(bool enabled);
	bool isParameterHighlightEnabled() const;
	void setNumberHighlightEnabled(bool enabled);
	bool isNumberHighlightEnabled() const;
	void setCommentHighlightEnabled(bool enabled);
	bool isCommentHighlightEnabled() const;
	void setStringHighlightEnabled(bool enabled);
	bool isStringHighlightEnabled() const;

	void setGCodeColor(const QColor &color);
	QColor gCodeColor() const;
	void setMCodeColor(const QColor &color);
	QColor mCodeColor() const;
	void setParameterColor(const QColor &color);
	QColor parameterColor() const;
	void setNumberColor(const QColor &color);
	QColor numberColor() const;
	void setCommentColor(const QColor &color);
	QColor commentColor() const;
	void setStringColor(const QColor &color);
	QColor stringColor() const;

protected:
	void highlightBlock(const QString &text) override;

private:
	bool gCodeHighlightEnabled;
	bool mCodeHighlightEnabled;
	bool parameterHighlightEnabled;
	bool numberHighlightEnabled;
	bool commentHighlightEnabled;
	bool stringHighlightEnabled;

	QTextCharFormat gCodeFormat;
	QTextCharFormat mCodeFormat;
	QTextCharFormat commentFormat;
	QTextCharFormat numberFormat;
	QTextCharFormat parameterFormat;
	QTextCharFormat stringFormat;

	void applyColors();
};

#endif // GCODEHIGHLIGHTER_H
