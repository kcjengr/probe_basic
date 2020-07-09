import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3

Rectangle {
    id: rectangle
    width: 1024
    height: 100
    color: "#939695"

    Row{
        visible: true
        Repeater {
            id: pocket_slot
            model: 12
            delegate: Item {

                id: pocket_item

                property string pocket_num: index+1

                Image {
                    id: fork
                    scale: 0.20
                    source: "images/linear_atc_fork.png"
                    x: (width/6 * index) - 200
                    y: -200
                    Rectangle {
                        id: pocket_rectangle

                        y: 265
                        x: 200
                        height: 100
                        width: height
                        color: "white"
                        radius: width/2
                        border.color: "black"
                        border.width: 4
                        Text {
                            id: pocket_text
                            text: "P" + pocket_item.pocket_num
                            font.family: "Bebas Kai"
                            font.bold: false
                            anchors.horizontalCenter: parent.horizontalCenter
                            anchors.top: parent.top
                            anchors.topMargin: 28
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            font.pixelSize: 48
                        }

                    }
                }

            }
        }
    }

    Row {
        visible: true
        Repeater {
            id: tool_slot
            model: 12

            delegate: Item {

                id: tool_item
                state: "visible"

                property int tool_num: index +1

                Rectangle {
                    id: tool_rectangle

                    width: 42
                    height: 42
                    radius: width/2
                    color: "white"
                    border.color: "grey"
                    border.width: 4

                    x: (83.4 * index) + 29
                    y: 12

                    Text {
                        id: tool_text
                        text: "T" + tool_item.tool_num
                        font.family: "Bebas Kai"
                        font.bold: false
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        font.pixelSize: 24
                        x: parent.width / 2 - width / 2
                        y: parent.height / 2 - height / 2
                    }
                }

                states: [
                    State {
                        name: "hidden"
                        PropertyChanges { target: tool_slot.itemAt(index); visible: false}
                    },
                    State {
                        name: "visible"
                        PropertyChanges { target: tool_slot.itemAt(index); visible: true}
                    }
                ]
            }
        }
    }


    property int prev_pocket: 1;



    Connections {
        target: atc_spiner;

        onHideToolSig: {
            tool_slot.itemAt(pocket - 1).state = "hidden";
        }

        onShowToolSig: {
            tool_slot.itemAt(pocket - 1).tool_num = tool_num;
            tool_slot.itemAt(pocket - 1).state = "visible";
        }

        onHomeMsgSig: {
            msg_text.text = message;
        }
    }
}
