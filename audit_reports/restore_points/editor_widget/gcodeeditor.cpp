#include "gcodeeditor.h"
#include <QScrollBar>
#include <QPainter>
#include <QTextBlock>
#include <QPalette>

void GCodeEditor::findDialog()
{
}

void GCodeEditor::saveFile()
{
}

void GCodeEditor::saveFileAs()
{
}

void GCodeEditor::EditorReadWrite(bool editable)
{
	setReadOnly(!editable);
}

GCodeEditor::GCodeEditor(QWidget *parent) : QPlainTextEdit(parent)
{
	highlighter = new GCodeHighlighter(document());
	lineNumberArea = new LineNumberArea(this);
	lineNumberAreaBackgroundColor = QColor(240, 240, 240);
	lineNumberAreaTextColor = Qt::black;
	lineNumberAreaFont = font();
	lineNumberAreaFont.setPointSize(10);
	currentLineHighlight = true;
	currentLineBackgroundColor = QColor(Qt::yellow).lighter(160);
	currentLineTextColor = palette().color(QPalette::Text);

	connect(document(), &QTextDocument::blockCountChanged,
			this, &GCodeEditor::updateLineNumberAreaWidth);
	connect(verticalScrollBar(), &QScrollBar::valueChanged,
			this, [this](int){ lineNumberArea->update(); });
	connect(this, &QPlainTextEdit::cursorPositionChanged,
			this, &GCodeEditor::highlightCurrentLine);

	updateLineNumberAreaWidth(0);
	highlightCurrentLine();
}

GCodeEditor::~GCodeEditor()
{
	delete highlighter;
}

int GCodeEditor::lineNumberAreaWidth() const
{
	int digits = 1;
	int max = qMax(1, document()->blockCount());
	while (max >= 10) {
		max /= 10;
		++digits;
	}
	QFontMetrics marginMetrics(lineNumberAreaFont);
	return 10 + marginMetrics.horizontalAdvance('9') * digits;
}

void GCodeEditor::lineNumberAreaPaintEvent(QPaintEvent *event)
{
	QPainter painter(lineNumberArea);
	painter.fillRect(event->rect(), lineNumberAreaBackgroundColor);
	painter.setFont(lineNumberAreaFont);

	QTextBlock block = firstVisibleBlock();
	int blockNumber = block.blockNumber();

	qreal top = blockBoundingGeometry(block).translated(contentOffset()).top();
	qreal bottom = top + blockBoundingRect(block).height();

	while (block.isValid() && top <= event->rect().bottom()) {
		if (block.isVisible() && bottom >= event->rect().top()) {
			QString number = QString::number(blockNumber + 1);
			painter.setPen(lineNumberAreaTextColor);
			painter.drawText(0, top,
							 lineNumberArea->width() - 5,
							 QFontMetrics(lineNumberAreaFont).height(),
							 Qt::AlignRight, number);
		}

		block = block.next();
		top = bottom;
		bottom = top + blockBoundingRect(block).height();
		++blockNumber;
	}
}

void GCodeEditor::resizeEvent(QResizeEvent *event)
{
	QPlainTextEdit::resizeEvent(event);

	QRect cr = contentsRect();
	lineNumberArea->setGeometry(QRect(cr.left(), cr.top(),
									  lineNumberAreaWidth(), cr.height()));
}

void GCodeEditor::updateLineNumberAreaWidth(int)
{
	setViewportMargins(lineNumberAreaWidth(), 0, 0, 0);
}

void GCodeEditor::highlightCurrentLine()
{
	QList<QTextEdit::ExtraSelection> extraSelections;

	if (!isReadOnly() && currentLineHighlight) {
		QTextEdit::ExtraSelection selection;
		selection.format.setBackground(currentLineBackgroundColor);
		selection.format.setForeground(currentLineTextColor);
		selection.format.setProperty(QTextFormat::FullWidthSelection, true);
		selection.cursor = textCursor();
		selection.cursor.clearSelection();
		extraSelections.append(selection);
	}

	setExtraSelections(extraSelections);
}

void GCodeEditor::updateLineNumberArea(const QRect &rect, int dy)
{
	if (dy)
		lineNumberArea->scroll(0, dy);
	else
		lineNumberArea->update(0, rect.y(), lineNumberArea->width(), rect.height());
}

bool GCodeEditor::gCodeHighlightEnabled() const
{
	return highlighter->isGCodeHighlightEnabled();
}

void GCodeEditor::setGCodeHighlightEnabled(bool enabled)
{
	highlighter->setGCodeHighlightEnabled(enabled);
}

bool GCodeEditor::mCodeHighlightEnabled() const
{
	return highlighter->isMCodeHighlightEnabled();
}

void GCodeEditor::setMCodeHighlightEnabled(bool enabled)
{
	highlighter->setMCodeHighlightEnabled(enabled);
}

bool GCodeEditor::parameterHighlightEnabled() const
{
	return highlighter->isParameterHighlightEnabled();
}

void GCodeEditor::setParameterHighlightEnabled(bool enabled)
{
	highlighter->setParameterHighlightEnabled(enabled);
}

bool GCodeEditor::numberHighlightEnabled() const
{
	return highlighter->isNumberHighlightEnabled();
}

void GCodeEditor::setNumberHighlightEnabled(bool enabled)
{
	highlighter->setNumberHighlightEnabled(enabled);
}

bool GCodeEditor::commentHighlightEnabled() const
{
	return highlighter->isCommentHighlightEnabled();
}

void GCodeEditor::setCommentHighlightEnabled(bool enabled)
{
	highlighter->setCommentHighlightEnabled(enabled);
}

bool GCodeEditor::stringHighlightEnabled() const
{
	return highlighter->isStringHighlightEnabled();
}

void GCodeEditor::setStringHighlightEnabled(bool enabled)
{
	highlighter->setStringHighlightEnabled(enabled);
}

QColor GCodeEditor::gCodeColor() const
{
	return highlighter->gCodeColor();
}

void GCodeEditor::setGCodeColor(const QColor &color)
{
	highlighter->setGCodeColor(color);
}

QColor GCodeEditor::mCodeColor() const
{
	return highlighter->mCodeColor();
}

void GCodeEditor::setMCodeColor(const QColor &color)
{
	highlighter->setMCodeColor(color);
}

QColor GCodeEditor::parameterColor() const
{
	return highlighter->parameterColor();
}

void GCodeEditor::setParameterColor(const QColor &color)
{
	highlighter->setParameterColor(color);
}

QColor GCodeEditor::numberColor() const
{
	return highlighter->numberColor();
}

void GCodeEditor::setNumberColor(const QColor &color)
{
	highlighter->setNumberColor(color);
}

QColor GCodeEditor::commentColor() const
{
	return highlighter->commentColor();
}

void GCodeEditor::setCommentColor(const QColor &color)
{
	highlighter->setCommentColor(color);
}

QColor GCodeEditor::stringColor() const
{
	return highlighter->stringColor();
}

void GCodeEditor::setStringColor(const QColor &color)
{
	highlighter->setStringColor(color);
}

QColor GCodeEditor::lineNumberAreaBackground() const
{
	return lineNumberAreaBackgroundColor;
}

void GCodeEditor::setLineNumberAreaBackground(const QColor &color)
{
	lineNumberAreaBackgroundColor = color;
	lineNumberArea->update();
}

QColor GCodeEditor::lineNumberAreaColor() const
{
	return lineNumberAreaTextColor;
}

void GCodeEditor::setLineNumberAreaColor(const QColor &color)
{
	lineNumberAreaTextColor = color;
	lineNumberArea->update();
}

QString GCodeEditor::lineNumberFontFamily() const
{
	return lineNumberAreaFont.family();
}

void GCodeEditor::setLineNumberFontFamily(const QString &family)
{
	lineNumberAreaFont.setFamily(family);
	updateLineNumberAreaWidth(0);
	lineNumberArea->update();
}

int GCodeEditor::lineNumberFontPointSize() const
{
	return lineNumberAreaFont.pointSize();
}

void GCodeEditor::setLineNumberFontPointSize(int pointSize)
{
	lineNumberAreaFont.setPointSize(pointSize);
	updateLineNumberAreaWidth(0);
	lineNumberArea->update();
}

int GCodeEditor::lineNumberFontWeight() const
{
	return lineNumberAreaFont.weight();
}

void GCodeEditor::setLineNumberFontWeight(int weight)
{
	lineNumberAreaFont.setWeight(static_cast<QFont::Weight>(weight));
	lineNumberArea->update();
}

bool GCodeEditor::lineNumberFontItalic() const
{
	return lineNumberAreaFont.italic();
}

void GCodeEditor::setLineNumberFontItalic(bool italic)
{
	lineNumberAreaFont.setItalic(italic);
	lineNumberArea->update();
}

bool GCodeEditor::currentLineHighlightEnabled() const
{
	return currentLineHighlight;
}

void GCodeEditor::setCurrentLineHighlightEnabled(bool enabled)
{
	currentLineHighlight = enabled;
	highlightCurrentLine();
}

QColor GCodeEditor::currentLineBackground() const
{
	return currentLineBackgroundColor;
}

void GCodeEditor::setCurrentLineBackground(const QColor &color)
{
	currentLineBackgroundColor = color;
	highlightCurrentLine();
}

QColor GCodeEditor::currentLineColor() const
{
	return currentLineTextColor;
}

void GCodeEditor::setCurrentLineColor(const QColor &color)
{
	currentLineTextColor = color;
	highlightCurrentLine();
}
