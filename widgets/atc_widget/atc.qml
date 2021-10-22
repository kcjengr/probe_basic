import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3

Rectangle {
    id: rectangle
    visible: true
    width: 550
    color: bg_color
    opacity: 1
    height: 550

    Image {
        id: atc_holder
        width: 550
        height: 550
        visible: true
        x: parent.width / 2 - width / 2
        y: parent.height / 2 - height / 2
        antialiasing: true
        z: 0
        rotation: 0
        transformOrigin: Item.Center
        source: "images/carousel_"+pocket_slots+".png"


        RotationAnimator {
            id: atc_anim
            target: atc_holder
            duration: anim_duration
            running: false
        }

        Repeater {
            id: pocket_slot
            model: pocket_slots
            rotation: 0

            delegate: Item {

                id: pocket_item

                height: atc_holder.height/2
                transformOrigin: Item.Bottom
                rotation: -index * 360/pocket_slots + 90
                x: atc_holder.width/2
                y: 0

                property string pocket_num: index+1
                property var anim: pocket_anim

                Rectangle {
                    id: pocket_rectangle

                    height: pocket_diam
                    width: pocket_diam
//                    radius: tool_diam/2
                    color: "white"
//                    border.color: "black"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.top
                    anchors.topMargin: pocket_position
                    border.width: 0
                    rotation: 360/pocket_slots * index - 90


                    Text {
                        id: pocket_text
                        text: "P" + pocket_item.pocket_num
                        font.family: "Bebas Kai"
                        font.bold: false
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        font.pixelSize: 24
                        x: parent.width / 2 - width / 2
                        y: parent.height / 2 - height / 2
                    }

                    RotationAnimation{
                        id:pocket_anim
                        target:pocket_text
                        direction: RotationAnimator.Shortest
                        duration: anim_duration
                        running: false
                    }
                }
            }
        }

        Repeater {
            id: tool_slot
            model: pocket_slots
            rotation: 0

            delegate: Item {

                id: tool_item
                height: atc_holder.height/2
                transformOrigin: Item.Bottom
                rotation: -index * 360/pocket_slots + 90
                x: atc_holder.width/2
                y: 0

                state: "visible"

                property int tool_num: index+1
                property var anim: tool_anim

                Rectangle {
                    id: tool_rectangle

                    height: tool_diam
                    width: tool_diam
                    radius: tool_diam/2
                    color: "white"
                    border.color: "grey"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.top
                    anchors.topMargin: 4
                    border.width: 2
                    rotation: 360/pocket_slots * index - 90

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

                    RotationAnimation {
                        id: tool_anim
                        target:tool_text
                        direction: RotationAnimator.Shortest
                        duration: anim_duration
                        running: false
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


    function rotate(steps, direction) {

        //        console.log("ROTATE")

        // console.log("ATC STEPS " + steps)

        if (direction === 1)
            anim_to = anim_from + (360/pocket_slots * steps);
        else if (direction === -1)
            anim_to = anim_from - (360/pocket_slots * steps);

        anim_duration = rotation_duration * steps;

        // console.log("ROTATE ATC FROM " + anim_from + " TO " + anim_to);
        rotate_atc(atc_anim, anim_duration, anim_from, anim_to);

        //        console.log("ROTATE TOOLS");

        for (var i = 0; i < (tool_slot.count); i++) {

            var tool_from = -anim_from;
            var tool_to = -anim_to;

            // console.log("ROTATE TOOL FROM " + tool_from + " TO " + tool_to);
            rotate_tool(tool_slot.itemAt(i), anim_duration, tool_from, tool_to);
        }

        // console.log("ROTATE POCKET SLOTS");

        for (var j = 0; j < pocket_slot.count; j++) {

            var pocket_from = -anim_from;
            var pocket_to = -anim_to;

            // console.log("ROTATE POCKET SLOT FROM " + pocket_from + " TO " + pocket_to);
            rotate_tool(pocket_slot.itemAt(j), anim_duration, pocket_from, pocket_to);
        }

        anim_from = anim_to;
    }

    Connections {
        target: atc_spiner;

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

        function onBgColorSig(color) {
            bg_color = color;
        }

        function onHideToolSig(pocket) {
            tool_slot.itemAt(pocket - 1).state = "hidden";
        }

        function onShowToolSig(pocket, tool_num) {
            tool_slot.itemAt(pocket - 1).tool_num = tool_num;
            tool_slot.itemAt(pocket - 1).state = "visible";
        }

        function onRotateSig(steps, direction) {
            rotate(steps, direction);
        }

        function onHomeMsgSig(message) {
            msg_text.text = message;
        }
    }
}
