import QtQuick 2.7
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Rectangle {

    id: main_rectangle
    visible: true
    color: bg_color
    width: widget_width
    height: 120
    z: 0


    Repeater {
        id: pocket_slot
        model: pocket_slots

        delegate: Item {

            id: pocket_item

            property string pocket_num: index+1
//            property var anim: pocket_anim

            Image {
                id: fork_image

                source: "images/rack_fork.png"


                fillMode: Image.PreserveAspectFit

                width: (main_rectangle.width/pocket_slots) -4
                height: 120

                x: (index * width) +2
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
                    color: "white"
                    border.color: "black"

                    x: parent.width / 2 - width / 2
                    y: parent.height / 2 - height / 2 + 24


                    transformOrigin: Item.Center

                    border.width: 1
                    z: 2
                    Text {
                        id: pocket_text
                        text: "P" + pocket_num
                        font.family: "Bebas Kai"
                        font.bold: true
                        x: parent.width / 2 - width / 2
                        y: parent.height / 2 - height / 2
                        //transformOrigin: Item.Center
                        //verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        font.pixelSize: 24

                        z: 3
                    }
//                rotation: 360/pocket_slots * index + 90
                }

            }
        }
	}
//    Repeater {
//        id: tool_slot
//        model: pocket_slots
//        rotation: 0

//        delegate: Item {

//            id: tool_item
//            height: atc_holder.height/2
//            transformOrigin: Item.Bottom
//            //rotation: -index * 360/pocket_slots + 90
//            x: atc_holder.width/2
//            y: 0

//            state: "visible"

//            property int tool_num: index+1
////            property var anim: tool_anim

//            Rectangle {
//                id: tool_rectangle

//                height: tool_diam
//                width: tool_diam
//                radius: tool_diam/2
//                color: "white"
//                border.color: "grey"
//                anchors.horizontalCenter: parent.horizontalCenter
//                anchors.top: parent.top
//                anchors.topMargin: 4
//                border.width: 2
//                // rotation: 360/pocket_slots * index - 90

//                Text {
//                    id: tool_text
//                    text: "T" + tool_item.tool_num
//                    font.family: "Bebas Kai"
//                    font.bold: false
//                    verticalAlignment: Text.AlignVCenter
//                    horizontalAlignment: Text.AlignHCenter
//                    font.pixelSize: 24
//                    x: parent.width / 2 - width / 2
//                    y: parent.height / 2 - height / 2
//                }

//            }

//            states: [
//                State {
//                    name: "hidden"
//                    PropertyChanges { target: tool_slot.itemAt(index); visible: false}
//                },
//                State {
//                    name: "visible"
//                    PropertyChanges { target: tool_slot.itemAt(index); visible: true}
//                }
//            ]
//        }
//    }


    function rotate_atc(anim, duration, from, to) {

        anim.duration = duration;
        anim.from = from;
        anim.to = to;
        anim.restart();
    }

    function rotate_tool(widget, duration, from, to) {

        widget.anim.duration = duration;
        widget.anim.from = from;
        widget.anim.to = to;
        widget.anim.restart();
    }

    // carousel size
    property int widget_width: 1024
    property int widget_height: 120

    // color properties
    property color bg_color: "grey"

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

    property int rotation_duration: 100;


//    function rotate(steps, direction) {

//        //        console.log("ROTATE")

//        // console.log("ATC STEPS " + steps)

//        if (direction === 1)
//            anim_to = anim_from + (360/pocket_slots * steps);
//        else if (direction === -1)
//            anim_to = anim_from - (360/pocket_slots * steps);

//        anim_duration = rotation_duration * Math.abs(steps);
        
//        // console.log("ROTATE ATC FROM " + anim_from + " TO " + anim_to);
//        rotate_atc(atc_anim, anim_duration, anim_from, anim_to);

//        //        console.log("ROTATE TOOLS");

//        for (var i = 0; i < (tool_slot.count); i++) {

//            var tool_from = -anim_from;
//            var tool_to = -anim_to;

//            // console.log("ROTATE TOOL FROM " + tool_from + " TO " + tool_to);
//            rotate_tool(tool_slot.itemAt(i), anim_duration, tool_from, tool_to);
//        }

//        // console.log("ROTATE POCKET SLOTS");

//        for (var j = 0; j < pocket_slot.count; j++) {

//            var pocket_from = -anim_from;
//            var pocket_to = -anim_to;

//            // console.log("ROTATE POCKET SLOT FROM " + pocket_from + " TO " + pocket_to);
//            rotate_tool(pocket_slot.itemAt(j), anim_duration, pocket_from, pocket_to);
//        }

//        anim_from = anim_to;
//    }

    Connections {
        target: atc_rack;

        function onAtcInitSig(pockets, step_duration) {
            rotation_duration = step_duration;

            pocket_slots = pockets;
            if (pocket_slots == 8) {
                pocket_position = 130;
                pocket_diam = 32;
                tool_diam = 85;
            }
            else if (pocket_slots == 10){
                pocket_position = 130;
                pocket_diam = 32;
                tool_diam = 85;
            }
            else if (pocket_slots == 12){
                pocket_position = 100;
                pocket_diam = 32;
                tool_diam = 70;
            }
            else if (pocket_slots == 14){
                pocket_position = 100;
                pocket_diam = 32;
                tool_diam = 63;
            }
            else if (pocket_slots == 16){
                pocket_position = 100;
                pocket_diam = 32;
                tool_diam = 67;
            }
            else if (pocket_slots == 18){
                pocket_position = 90;
                pocket_diam = 32;
                tool_diam = 60;
            }
            else if (pocket_slots == 20){
                pocket_position = 80;
                pocket_diam = 32;
                tool_diam = 55;
            }
            else if (pocket_slots == 21){
                pocket_position = 80;
                pocket_diam = 32;
                tool_diam = 50;
            }
            else if (pocket_slots == 24){
                pocket_position = 70;
                pocket_diam = 32;
                tool_diam = 45;
            }
        }

        function onResizeSig(width, height) {
            widget_width = width;
            widget_height = height;
            pocket_position = width - ((width/2) * 0.5);
            tool_diam = width/ 7.85;
        }

        function onBgColorSig(color) {
            bg_color = color;
        }

//        function onHideToolSig(pocket) {
//            tool_slot.itemAt(pocket - 1).state = "hidden";
//        }

//        function onShowToolSig(pocket, tool_num) {
//            tool_slot.itemAt(pocket - 1).tool_num = tool_num;
//            tool_slot.itemAt(pocket - 1).state = "visible";
//        }

//        function onRotateSig(steps, direction) {
//            rotate(steps, direction);
//        }

//        function onHomeMsgSig(message) {
//            msg_text.text = message;
//        }
    }
}
