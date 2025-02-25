import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Rectangle {

    id: main_rectangle
    visible: true
    color: bg_color
    width: parent ? parent.width : widget_width
    height: 129  // Set to exact image height
    z: 0

    // Image dimension properties
    property int imageWidth: 115
    property int imageHeight: 129
    property real widget_width: 1510
    property real exactWidth: imageWidth  // Use actual image width

    // Scaling and spacing properties
    property real minSpacing: 5  // Minimum spacing between items
    property real minScale: 0.5
    
    // First calculate total space needed at minimum scale
    property real minTotalWidth: (imageWidth * minScale * pocket_slots) + (minSpacing * (pocket_slots - 1))
    
    // Calculate scale factor ensuring we fit within widget_width
    property real scaleFactor: Math.min(1.0, widget_width / ((imageWidth * pocket_slots) + (minSpacing * (pocket_slots - 1))))
    
    // Calculate final dimensions
    property real scaledImageWidth: imageWidth * scaleFactor
    property real usedWidth: (scaledImageWidth * pocket_slots)
    property real availableSpace: widget_width - usedWidth
    property real spacing: availableSpace / (pocket_slots - 1)

    // Debug output
    Component.onCompleted: {
        console.log("Widget width:", widget_width)
        console.log("Min total width needed:", minTotalWidth)
        console.log("Scale factor:", scaleFactor)
        console.log("Scaled image width:", scaledImageWidth)
        console.log("Total used width:", usedWidth + (spacing * (pocket_slots - 1)))
        console.log("Spacing between:", spacing)
        console.log("Actual Rectangle width:", width)
        console.log("Parent width:", parent ? parent.width : "no parent")
        console.log("Container item width:", container.width)
        console.log("Main window width:", window ? window.width : "no window")
    }

    // Add width change monitoring
    onWidthChanged: {
        console.log("Widget width changed to:", width)
        console.log("Parent width:", parent ? parent.width : "no parent")
        console.log("Container width:", container.width)
    }

    // Layout container
    Item {
        id: container
        anchors.fill: parent

        // Fixed dimensions
        property real imageSpace: imageWidth
        property real fullContentWidth: imageSpace * pocket_slots

        // Scale based on available width
        property real scaleToFit: Math.min(1.0, width / fullContentWidth)
        property real scaledWidth: imageSpace * scaleToFit
        property real spaceBetween: (width - (scaledWidth * pocket_slots)) / (pocket_slots - 1)

        onWidthChanged: {
            console.log("Container width:", width)
            console.log("Full content width:", fullContentWidth)
            console.log("Scale:", scaleToFit)
            console.log("Item width:", scaledWidth)
            console.log("Space between:", spaceBetween)
            console.log("Total used:", (scaledWidth * pocket_slots) + (spaceBetween * (pocket_slots - 1)))
        }

        // Fork images
        Repeater {
            id: pocket_slot
            model: pocket_slots
            delegate: Item {
                id: pocket_item
                property string pocket_num: index + 1

                Image {
                    id: fork_image
                    source: "images/rack_fork.png"
                    width: imageWidth
                    height: imageHeight
                    scale: container.scaleToFit

                    // Position each item with exact spacing
                    x: index * (container.scaledWidth + container.spaceBetween)
                    transformOrigin: Item.TopLeft

                    Rectangle {

                        id: pocket_rectangle
                        opacity: 1
                        width: 36
                        height: 28
                        color: "transparent"
                        border.color: "transparent"
                        x: parent.width / 2 - width / 2
                        y: parent.height / 2 - height / 2 + 40
                        transformOrigin: Item.Center
                        border.width: 1
                        z: 2
                        scale: 1/scaleFactor  // Counter-scale text to maintain size
                        Text {
                            id: pocket_text
                            color: "white"
                            text: "P" + parent.parent.parent.pocket_num  // Fix pocket number reference
                            font.family: "Bebas Kai"
                            font.bold: true
                            x: parent.width / 2 - width / 2
                            y: parent.height / 2 - height / 2
                            horizontalAlignment: Text.AlignHCenter
                            font.pixelSize: 22  // Fixed size instead of scaled
                            z: 3
                        }
                    }
                }
            }
        }

        // Tool slots
        Repeater {
            id: tool_slot
            model: pocket_slots
            delegate: Item {
                id: tool_item
                
                // Position using same calculation as fork images
                x: index * (container.scaledWidth + container.spaceBetween)
                y: 0
                width: container.scaledWidth
                height: imageHeight * container.scaleToFit
                
                property int tool_num: index+1
                state: "visible"

                Rectangle {
                    id: tool_rectangle
                    
                    // Center in scaled parent item
                    anchors {
                        horizontalCenter: parent.horizontalCenter
                        verticalCenter: parent.verticalCenter
                        verticalCenterOffset: -27 * container.scaleToFit
                    }
                    
                    // Scale dimensions with container
                    width: tool_diam * container.scaleToFit
                    height: tool_diam * container.scaleToFit
                    radius: width/2
                    
                    color: "white"
                    border.color: "grey"
                    border.width: 2
                    z: 2

                    Text {
                        id: tool_text
                        anchors.centerIn: parent
                        text: "T" + tool_item.tool_num
                        font.family: "Bebas Kai"
                        font.bold: false
                        font.pixelSize: 22
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
        target: rack_atc;

        function onAtcInitSig(pockets) {
            pocket_slots = pockets
            console.log(pockets)
        }

        function onHideToolSig(pocket) {
            tool_slot.itemAt(pocket - 1).state = "hidden";
        }

        function onShowToolSig(pocket, tool_num) {
            tool_slot.itemAt(pocket - 1).tool_num = tool_num;
            tool_slot.itemAt(pocket - 1).state = "visible";
        }


//        function onResizeSig(width, height) {
//            widget_width = width  // This will propagate through the single width binding
//            widget_height = height
//            // Recalculate spacing when width changes
//            availableSpace = widget_width - (imageWidth * pocket_slots)
//            calculatedSpacing = availableSpace / (pocket_slots - 1)
//        }

        function onBgColorSig(color) {
            bg_color = color;
        }
    }
}
