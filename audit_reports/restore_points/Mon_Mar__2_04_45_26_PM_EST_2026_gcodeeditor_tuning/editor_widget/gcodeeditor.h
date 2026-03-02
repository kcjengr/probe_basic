#ifndef GCODEEDITOR_H
#define GCODEEDITOR_H

#include <QPlainTextEdit>
#include <QPainter>
#include <QTextBlock>
#include <QColor>
#include <QFont>
#include "gcodehighlighter.h"

class LineNumberArea;

class GCodeEditor : public QPlainTextEdit
{
	Q_OBJECT
	Q_PROPERTY(bool gCodeHighlightEnabled READ gCodeHighlightEnabled WRITE setGCodeHighlightEnabled)
	Q_PROPERTY(bool mCodeHighlightEnabled READ mCodeHighlightEnabled WRITE setMCodeHighlightEnabled)
	Q_PROPERTY(bool parameterHighlightEnabled READ parameterHighlightEnabled WRITE setParameterHighlightEnabled)
	Q_PROPERTY(bool numberHighlightEnabled READ numberHighlightEnabled WRITE setNumberHighlightEnabled)
	Q_PROPERTY(bool commentHighlightEnabled READ commentHighlightEnabled WRITE setCommentHighlightEnabled)
	Q_PROPERTY(bool stringHighlightEnabled READ stringHighlightEnabled WRITE setStringHighlightEnabled)

	Q_PROPERTY(QColor gCodeColor READ gCodeColor WRITE setGCodeColor)
	Q_PROPERTY(QColor mCodeColor READ mCodeColor WRITE setMCodeColor)
	Q_PROPERTY(QColor parameterColor READ parameterColor WRITE setParameterColor)
	Q_PROPERTY(QColor numberColor READ numberColor WRITE setNumberColor)
	Q_PROPERTY(QColor commentColor READ commentColor WRITE setCommentColor)
	Q_PROPERTY(QColor stringColor READ stringColor WRITE setStringColor)

	Q_PROPERTY(QColor lineNumberAreaBackground READ lineNumberAreaBackground WRITE setLineNumberAreaBackground)
	Q_PROPERTY(QColor lineNumberAreaColor READ lineNumberAreaColor WRITE setLineNumberAreaColor)
	Q_PROPERTY(QString lineNumberFontFamily READ lineNumberFontFamily WRITE setLineNumberFontFamily)
	Q_PROPERTY(int lineNumberFontPointSize READ lineNumberFontPointSize WRITE setLineNumberFontPointSize)
	Q_PROPERTY(int lineNumberFontWeight READ lineNumberFontWeight WRITE setLineNumberFontWeight)
	Q_PROPERTY(bool lineNumberFontItalic READ lineNumberFontItalic WRITE setLineNumberFontItalic)

	Q_PROPERTY(bool currentLineHighlightEnabled READ currentLineHighlightEnabled WRITE setCurrentLineHighlightEnabled)
	Q_PROPERTY(QColor currentLineBackground READ currentLineBackground WRITE setCurrentLineBackground)
	Q_PROPERTY(QColor currentLineColor READ currentLineColor WRITE setCurrentLineColor)

public:
	explicit GCodeEditor(QWidget *parent = nullptr);
	~GCodeEditor();

	int lineNumberAreaWidth() const;
	void lineNumberAreaPaintEvent(QPaintEvent *event);

	bool gCodeHighlightEnabled() const;
	void setGCodeHighlightEnabled(bool enabled);
	bool mCodeHighlightEnabled() const;
	void setMCodeHighlightEnabled(bool enabled);
	bool parameterHighlightEnabled() const;
	void setParameterHighlightEnabled(bool enabled);
	bool numberHighlightEnabled() const;
	void setNumberHighlightEnabled(bool enabled);
	bool commentHighlightEnabled() const;
	void setCommentHighlightEnabled(bool enabled);
	bool stringHighlightEnabled() const;
	void setStringHighlightEnabled(bool enabled);

	QColor gCodeColor() const;
	void setGCodeColor(const QColor &color);
	QColor mCodeColor() const;
	void setMCodeColor(const QColor &color);
	QColor parameterColor() const;
	void setParameterColor(const QColor &color);
	QColor numberColor() const;
	void setNumberColor(const QColor &color);
	QColor commentColor() const;
	void setCommentColor(const QColor &color);
	QColor stringColor() const;
	void setStringColor(const QColor &color);

	QColor lineNumberAreaBackground() const;
	void setLineNumberAreaBackground(const QColor &color);
	QColor lineNumberAreaColor() const;
	void setLineNumberAreaColor(const QColor &color);
	QString lineNumberFontFamily() const;
	void setLineNumberFontFamily(const QString &family);
	int lineNumberFontPointSize() const;
	void setLineNumberFontPointSize(int pointSize);
	int lineNumberFontWeight() const;
	void setLineNumberFontWeight(int weight);
	bool lineNumberFontItalic() const;
	void setLineNumberFontItalic(bool italic);

	bool currentLineHighlightEnabled() const;
	void setCurrentLineHighlightEnabled(bool enabled);
	QColor currentLineBackground() const;
	void setCurrentLineBackground(const QColor &color);
	QColor currentLineColor() const;
	void setCurrentLineColor(const QColor &color);

public slots:
	void findDialog();
	void saveFile();
	void saveFileAs();
	void EditorReadWrite(bool editable);

protected:
	void resizeEvent(QResizeEvent *event) override;

private:
	GCodeHighlighter *highlighter;
	QWidget *lineNumberArea;
	QColor lineNumberAreaBackgroundColor;
	QColor lineNumberAreaTextColor;
	QFont lineNumberAreaFont;
	bool currentLineHighlight;
	QColor currentLineBackgroundColor;
	QColor currentLineTextColor;

	void updateLineNumberAreaWidth(int newBlockCount);
	void highlightCurrentLine();
	void updateLineNumberArea(const QRect &rect, int dy);

	friend class LineNumberArea;
};

class LineNumberArea : public QWidget
{
public:
	LineNumberArea(GCodeEditor *editor) : QWidget(editor), editor(editor) {}

	QSize sizeHint() const override {
		return QSize(editor->lineNumberAreaWidth(), 0);
	}

protected:
	void paintEvent(QPaintEvent *event) override {
		editor->lineNumberAreaPaintEvent(event);
	}

private:
	GCodeEditor *editor;
};

#endif // GCODEEDITOR_H
