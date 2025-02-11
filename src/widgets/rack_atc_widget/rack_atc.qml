import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Rectangle {

    id: main_rectangle
    visible: true
    color: bg_color
    width: widget_width
    height: 129  // Set to exact image height
    z: 0

    // Image dimension properties
    property int imageWidth: 115
    property int imageHeight: 129
    property int spacing: 5
    property real widget_width: 1540
    property real exactWidth: imageWidth  // Use actual image width
    property real availableSpace: widget_width - (imageWidth * pocket_slots)
    property real calculatedSpacing: availableSpace / (pocket_slots - 1)

    Repeater {
        id: pocket_slot
        model: pocket_slots    // This determines how many items are created

        delegate: Item {

            id: pocket_item

            property string pocket_num: index+1
            // ...existing code...

            Image {
                id: fork_image

                source: "images/rack_fork.png"


                fillMode: Image.PreserveAspectFit

                width: imageWidth
                height: imageHeight

                // Simple centering calculation
                x: index * (imageWidth + calculatedSpacing)
                transformOrigin: Item.Center
                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter
                z: 1

                Rectangle {

                    id: pocket_rectangle
                    opacity: 1
                    width: 36
                    height: 28
    //                    radius: tool_diam/2
                    color: "transparent"
                    border.color: "transparent"
                    x: parent.width / 2 - width / 2
                    y: parent.height / 2 - height / 2 + 40
                    transformOrigin: Item.Center
                    border.width: 1
                    z: 2
                    Text {
                        id: pocket_text
                        color: "white"
                        text: "P" + pocket_num
                        font.family: "Bebas Kai"
                        font.bold: true
                        x: parent.width / 2 - width / 2
                        y: parent.height / 2 - height / 2
                        //transformOrigin: Item.Center
                        //verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        font.pixelSize: 24  // Fixed size instead of scaled
                        z: 3
                    }
//                rotation: 360/pocket_slots * index + 90
                }

            }
        }
	}
    Repeater {
        id: tool_slot
        model: pocket_slots
        
        delegate: Item {
            id: tool_item
            
            // Position tool items at same x coordinates as fork images
            x: index * (imageWidth + calculatedSpacing)
            y: 0
            width: imageWidth  // Match parent width
            height: imageHeight  // Match parent height
            
            property int tool_num: index+1
            state: "visible"

            Rectangle {
                id: tool_rectangle
                
                // Center in parent item
                anchors.horizontalCenter: parent.horizontalCenter
                y: parent.height / 2 - 59  // Position above pocket text
                
                height: tool_diam
                width: tool_diam
                radius: tool_diam/2
                color: "white"
                border.color: "grey"
                border.width: 2
                z: 2  // Above fork image but below text

                Text {
                    id: tool_text
                    anchors.centerIn: parent  // Center in tool rectangle
                    text: "T" + tool_item.tool_num
                    font.family: "Bebas Kai"
                    font.bold: false
                    font.pixelSize: 24
                }
            }

            states: [
                State {
                    name: "hidden"
                    PropertyChanges { target: tool_rectangle; visible: false}
                },
                State {
                    name: "visible"
                    PropertyChanges { target: tool_rectangle; visible: true}
                }
            ]
        }
    }

    // carousel size
    property int widget_height: 129

    // color properties
    property color bg_color: "#929695"

    // Animation Properties
    property int anim_from: 0;
    property int anim_to: 0;
    property int anim_duration: 0;

    // Carousel Properties
    property int pocket_slots: 12;

    property int pocket_position: 100;
    property int pocket_diam: 32;
    property int tool_diam: 70;

    property int prev_pocket: 1;

    Connections {
        target: qml_rack_widget;

        function onAtcInitSig(pockets) {
        }

        function onResizeSig(width, height) {
            widget_width = width  // This will propagate through the single width binding
            widget_height = height
            // Recalculate spacing when width changes
            availableSpace = widget_width - (imageWidth * pocket_slots)
            calculatedSpacing = availableSpace / (pocket_slots - 1)
        }

        function onBgColorSig(color) {
            bg_color = color;
        }
    }
}
