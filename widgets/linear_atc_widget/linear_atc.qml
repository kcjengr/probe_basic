import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3

Rectangle {
    id: rectangle
    width: 1024
    height: 340
    color: "#939695"

    Row{
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
                    x: (width/6 * index) -200
                    y: 20
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
        Repeater {
            id: tool_slot
            width: 200
            height: 200
            model: 12

            delegate: Item {

                id: tool_item
                height: atc_holder.height/2
                transformOrigin: Item.Bottom
                x: atc_holder.width/2
                y: 0

                state: "hidden"

                property int tool_num: index
                property var anim: tool_anim

                Rectangle {
                    id: tool_rectangle

                    height: atc_holder.height*0.135
                    width: height
                    radius: width/2
                    color: "white"
                    border.color: "grey"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.top
                    anchors.topMargin: 4
                    border.width: 2

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

    Text {
        id: msg_text
        width: 206
        height: 91
        x: parent.width/2 - width/2
        y: parent.height/2 - height/2
        text: qsTr("UN REFERENCED")
        visible: true
        font.capitalization: Font.AllUppercase
        font.pixelSize: 36
        font.family: "Bebas Kai"
        fontSizeMode: Text.Fit
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter

        Behavior on text {
            FadeAnimation {
                target: msg_text
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
