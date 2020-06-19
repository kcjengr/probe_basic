import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3

Rectangle {
    visible: true
    width: 1024
    clip: false
    transformOrigin: Item.Center
    height: 600
    color: "#939695"
    border.color: "#00000000"

    Image {
        id: holder
        x: 0
        y: 140
        width: 452
        height: 321
        fillMode: Image.PreserveAspectCrop
        z: 0
        rotation: 0
        transformOrigin: Item.Center
        source: "images/lathe_chuck_dim_lines.png"
    }

    Row {
        id: upper_row
        x: 308
        y: -89
        width: 459
        height: 336
        spacing: 20; // a simple layout do avoid overlapping

            Repeater {
                id: upper_tools
                model: 5; // just define the number you want, can be a variable too

                delegate:
                    Image {
                        x: 380
                        y: 0
                        width: 50
                        height: 200
                        fillMode: Image.PreserveAspectFit
                        z: 0
                        rotation: 0
                        state: "released"
                        source: "images/lathe_center_turning_rp_bs.png"
                        property real origin_x: 0.0
                        property real origin_y: 0.0

//                        MouseArea {
//                            anchors.fill: parent
//                            onClicked: {
//                                tool_selected(upper_tools.itemAt(index), "upper", index)
//                            }
//                        }
                        states: [
                            State {
                                name: "hidden"
                                PropertyChanges { target: upper_tools.itemAt(index); x: 70*index ; y: -180 }
                            },
                            State {
                                name: "released"
                                PropertyChanges { target: upper_tools.itemAt(index); x: 70*index ; y: 0 }
                            },
                            State {
                                name: "selected"
                                PropertyChanges { target: upper_tools.itemAt(index); x: 65 + origin_x; y: 135 + origin_y }
                            }
                        ]
                        transitions: Transition {
                            NumberAnimation{ properties: "x,y"; easing.type: Easing.OutExpo }
                        }
                   }
            }
        }

    Row {
        id: lower_row
        x: 308
        y: 351
        width: 467
        height: 389
        spacing: 20; // a simple layout do avoid overlapping

            Repeater {
                id: lower_tools
                model: 5; // just define the number you want, can be a variable too

                delegate:
                    Image {
                        x: 380
                        y: 0
                        width: 50
                        height: 200
                        fillMode: Image.PreserveAspectFit
                        z: 0
                        rotation: 0
                        state: "released"
                        source: "images/lathe_center_turning_fp_ts.png"
                        property real origin_x: 0.0
                        property real origin_y: 0.0

//                        MouseArea {
//                            anchors.fill: parent
//                            onClicked: {
//                                tool_selected(lower_tools.itemAt(index), "lower", index)
//                            }
//                        }
                        states: [
                            State {
                                name: "hidden"
                                PropertyChanges { target: lower_tools.itemAt(index); x: 70*index ; y: +300 }
                            },
                            State {
                                name: "released"
                                PropertyChanges { target: lower_tools.itemAt(index); x: 70*index; y: 100 }
                            },
                            State {
                                name: "selected"
                                PropertyChanges { target: lower_tools.itemAt(index); x: 65 + origin_x; y: 5 + origin_y }
                            }
                        ]
                        transitions: Transition {
                            NumberAnimation{ properties: "x,y"; easing.type: Easing.OutExpo }
                        }
                   }
            }
        }

    Column {
        id: right_column
        x: 308
        y: 166
        width: 199
        height: 269
        spacing: 20; // a simple layout do avoid overlapping

            Repeater {
                id: right_tools
                model: 5; // just define the number you want, can be a variable too

                delegate:
                    Image {
                        x: 0
                        y: 0
                        width: 200
                        height: 38
                        fillMode: Image.PreserveAspectFit
                        z: 0
                        rotation: 0
                        state: "released"
                        source: "images/lathe_internal_threading_bs.png"
                        property real origin_x: 0.0
                        property real origin_y: 0.0


//                        MouseArea {
//                            anchors.fill: parent
//                            onClicked: {
//                                tool_selected(right_tools.itemAt(index), "right", index)
//                            }
//                        }
                        states: [
                            State {
                                name: "hidden"
                                PropertyChanges { target: right_tools.itemAt(index); x: 800 ; y: 58*index }
                            },
                            State {
                                name: "released"
                                PropertyChanges { target: right_tools.itemAt(index); x: 500; y: 58*index }
                            },
                            State {
                                name: "selected"
                                PropertyChanges { target: right_tools.itemAt(index); x: 65 + origin_x; y: 116 + origin_y }
                            }
                        ]
                        transitions: Transition {
                            NumberAnimation{ properties: "x,y"; easing.type: Easing.OutExpo }
                        }
                    }
            }
        }




    Component.onCompleted: {

        var upper_tool_pics = [
            "images/lathe_lh_turning_rp_bs.png",
            "images/lathe_center_turning_rp_bs.png",
            "images/lathe_rh_turning_rp_bs.png",
            "images/lathe_lh_threading_rp_ts.png",
            "images/lathe_rh_parting_rp_bs.png"
        ];

        var lower_tool_pics = [
            "images/lathe_lh_turning_fp_ts.png",
            "images/lathe_center_turning_fp_ts.png",
            "images/lathe_rh_turning_fp_ts.png",
            "images/lathe_rh_threading_fp_ts.png",
            "images/lathe_parting_fp_ts.png"
        ];

        var right_tool_pics = [
            "images/lathe_internal_threading_bs.png",
            "images/lathe_internal_boring_bs.png",
            "images/lathe_internal_drilling_ts.png",
            "images/lathe_internal_boring_ts.png",
            "images/lathe_internal_threading_ts.png"
        ];

        var upper_tool_origins = [
                    [-50, 0],
                    [-25, 0],
                    [0, 0],
                    [0, 0],
                    [0, 0]
        ];

        var lower_tool_origins = [
                    [-50, 0],
                    [-25, 0],
                    [0, 0],
                    [0, 0],
                    [0, 0]
        ];

        var right_tool_origins = [
                    [0, -29],
                    [0, -29],
                    [0, 0],
                    [0, 29],
                    [0, 29]
        ];

        set_element_properties(upper_tools, upper_tool_pics, upper_tool_origins);
        set_element_properties(lower_tools, lower_tool_pics, lower_tool_origins);
        set_element_properties(right_tools, right_tool_pics, right_tool_origins);
    }


    function set_element_properties(element, pics, origin) {
        for (var i = 0; i < 5; i++) {
            console.log(origin[i]);
            element.itemAt(i).origin_x = origin[i][0];
            element.itemAt(i).origin_y = origin[i][1];
            element.itemAt(i).source = pics[i];
        }
    }


    function tool_selected(tool, group, index) {

        // handler.selected_tool(group, index)

        if (tool.state === "selected") {
            for (var i = 0; i < 5; i++){
                upper_tools.itemAt(i).state = "released"
                lower_tools.itemAt(i).state = "released"
                right_tools.itemAt(i).state = "released"
            }
        }
        else {
            for (var j = 0; j < 5; j++){
                upper_tools.itemAt(j).state = "hidden"
                lower_tools.itemAt(j).state = "hidden"
                right_tools.itemAt(j).state = "hidden"
            }
            tool.state  = "selected"
        }
    }

    Connections {
        target: handler

        onToolSig: {
            var tool_in_spindle = 0

            if ((active_tool >= 0) && (active_tool <= 4)){
                tool_in_spindle = active_tool
                tool_selected(lower_tools.itemAt(tool_in_spindle), "lower", tool_in_spindle)
            }
            else if ((active_tool >= 5) && (active_tool <= 9)){
                tool_in_spindle = active_tool - 5
                tool_selected(upper_tools.itemAt(tool_in_spindle), "upper", tool_in_spindle)
            }
            else if ((active_tool >= 10) && (active_tool <= 14)){
                tool_in_spindle = active_tool - 10
                tool_selected(right_tools.itemAt(tool_in_spindle), "right", tool_in_spindle)
            }

        }
    }
}
