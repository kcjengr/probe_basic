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
        width: 304
        height: 321
        fillMode: Image.PreserveAspectCrop
        z: 0
        rotation: 0
        transformOrigin: Item.Center
        source: "images/lathe_chuck_stock.png"
    }

    Image {
        id: bottom_horizontal_dimensions
        x: 257
        y: 351
        z: 0
        visible: false
        width: 165
        height: 90
        fillMode: Image.PreserveAspectCrop
        rotation: 0
        transformOrigin: Item.Center
        source: "images/lathe_horizontal_dimension.png"
    }

    Image {
        id: top_horizontal_dimensions
        x: 260
        y: 159
        z: 0
        visible: false
        width: 165
        height: 90
        fillMode: Image.PreserveAspectCrop
        rotation: 180
        transformOrigin: Item.Center
        source: "images/lathe_horizontal_dimension.png"
    }

    Image {
        id: vertical_dimensions
        x: 372
        y: 197
        z: 0
        visible: false
        width: 87
        height: 207
        fillMode: Image.PreserveAspectCrop
        rotation: 0
        transformOrigin: Item.Center
        source: "images/lathe_vertical_dimension.png"
    }

    Rectangle{
        id: tool_origin_top_left
        visible: false
        x: 400
        y: 120
        width: 125
        height: 125
        border.color: "black"
        border.width: 2
        radius: 16
        color: "white"
        transformOrigin: Item.Center

        MouseArea {
            anchors.fill: parent
            onClicked: {
                choose_option("left")
            }
        }

        Image {
            x: 10
            y: 10
            z: 0
            width: 100
            height: 100
            fillMode: Image.PreserveAspectCrop
            rotation: 0
            transformOrigin: Item.Center
            source: "images/groove_tool_2.png"
        }
    }

    Rectangle{
        id: tool_origin_top_right
        visible: false
        x: 650
        y: 120
        z: 0
        width: 125
        height: 125
        border.color: "black"
        border.width: 2
        radius: 16
        color: "white"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                choose_option("right")
            }
        }

        Image {
            x: 10
            y: 10
            z: 0
            width: 100
            height: 100
            fillMode: Image.PreserveAspectCrop
            rotation: 0
            source: "images/groove_tool_1.png"
        }
    }

    Rectangle{
        id: tool_origin_bot_left
        visible: false
        x: 400
        y: 140
        z: 0
        width: 125
        height: 125
        border.color: "black"
        border.width: 2
        radius: 16
        color: "white"
        transformOrigin: Item.Center

        MouseArea {
            anchors.fill: parent
            onClicked: {
                choose_option("left")
            }
        }

        Image {
            x: 10
            y: 10
            z: 0
            width: 100
            height: 100
            fillMode: Image.PreserveAspectCrop
            rotation: 0
            transformOrigin: Item.Center
            source: "images/groove_tool_3.png"
        }
    }

    Rectangle{
        id: tool_origin_bot_right
        visible: false
        x: 650
        y: 140
        z: 0
        width: 125
        height: 125
        border.color: "black"
        border.width: 2
        radius: 16
        color: "white"
        transformOrigin: Item.Center

        MouseArea {
            anchors.fill: parent
            onClicked: {
                choose_option("right")
            }
        }

        Image {
            x: 10
            y: 10
            z: 0
            width: 100
            height: 100
            fillMode: Image.PreserveAspectCrop
            rotation: 0
            transformOrigin: Item.Center
            source: "images/groove_tool_4.png"
        }
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

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        tool_selected(upper_tools.itemAt(index), "upper", index, true)
                    }
                }
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
                    },
                    State {
                        name: "option"
                        PropertyChanges { target: upper_tools.itemAt(index); x: 260 + origin_x; y: 100 + origin_y }
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

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        tool_selected(lower_tools.itemAt(index), "lower", index, true)
                    }
                }
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
                    },
                    State {
                        name: "option"
                        PropertyChanges { target: lower_tools.itemAt(index); x: 260 + origin_x; y: -100 + origin_y }
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
        y: 90
        width: 199
        height: 269
        spacing: 20; // a simple layout do avoid overlapping

        Repeater {
            id: right_tools
            model: 7; // just define the number you want, can be a variable too

            delegate:
                Image {
                x: 0
                y: 0
                width: 200
                height: 42
                fillMode: Image.PreserveAspectFit
                z: 0
                rotation: 0
                state: "released"
                source: "images/lathe_internal_threading_bs.png"
                property real origin_x: 0.0
                property real origin_y: 0.0


                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        tool_selected(right_tools.itemAt(index), "right", index, true)
                    }
                }
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
                        PropertyChanges { target: right_tools.itemAt(index); x: 65 + origin_x; y: 192 + origin_y }
                    },
                    State {
                        name: "option"
                        PropertyChanges { target: right_tools.itemAt(index); x: 240 + origin_x; y: 240 + origin_y }
                    }
                ]
                transitions: Transition {
                    NumberAnimation{ properties: "x,y"; easing.type: Easing.OutExpo }
                }
            }
        }
    }

    Item {
        id: options
        property string selected_group: ""
        property int selected_index: 0
        property var orientation_table: {
            "upper": {'0':4, '1':8, '2':3, '3':8},
            "lower": {'0':1, '1':6, '2':2, '3':6},
            "right": {'1':6, '2':2, '3':9, '4':3, '5':8}
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
                    "images/lathe_rh_internal_grooving_bs.png",
                    "images/lathe_internal_threading_bs.png",
                    "images/lathe_internal_boring_bs.png",
                    "images/lathe_internal_drilling_ts.png",
                    "images/lathe_internal_boring_ts.png",
                    "images/lathe_internal_threading_ts.png",
                    "images/lathe_rh_internal_grooving.png"
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
                    [0, -29],
                    [0, 0],
                    [0, 29],
                    [0, 29],
                    [0, 29]
                ];

        set_element_properties(upper_tools, upper_tool_pics, upper_tool_origins);
        set_element_properties(lower_tools, lower_tool_pics, lower_tool_origins);
        set_element_properties(right_tools, right_tool_pics, right_tool_origins);



    }

    function set_element_properties(element, pics, origin) {
        for (var i = 0; i < element.model; i++) {
            element.itemAt(i).origin_x = origin[i][0]
            element.itemAt(i).origin_y = origin[i][1]
            element.itemAt(i).source = pics[i];
        }
    }


    function tool_selected(tool, group, index, tool_options) {

        var orientation = options.orientation_table[group][String(index)]

        options.selected_group = group
        options.selected_index = index

        if (tool.state === "selected") {
            for (var i = 0; i < 5; i++){
                upper_tools.itemAt(i).state = "released"
                lower_tools.itemAt(i).state = "released"
            }
            for (var j = 0; j < 7; j++){
                right_tools.itemAt(j).state = "released"
            }
            handler.tool_select(group, index, orientation)

            top_horizontal_dimensions.visible = false
            bottom_horizontal_dimensions.visible = false
            vertical_dimensions.visible = false
        }
        else if (tool.state === "option"){

            for (var k = 0; k < 5; k++){
                upper_tools.itemAt(k).state = "released"
                lower_tools.itemAt(k).state = "released"
            }
            for (var l = 0; l < 7; l++){
                right_tools.itemAt(l).state = "released"
            }

            tool_origin_top_left.visible = false
            tool_origin_top_right.visible = false

            tool_origin_bot_left.visible = false
            tool_origin_bot_right.visible = false
        }

        else {
            for (var m = 0; m < 5; m++){
                upper_tools.itemAt(m).state = "hidden"
                lower_tools.itemAt(m).state = "hidden"
            }
            for (var n = 0; n < 7; n++){
                right_tools.itemAt(n).state = "hidden"
            }

            if (group === "upper"){
                if (index === 4){
                    if (tool_options === false){
                        tool.state  = "selected"
                        top_horizontal_dimensions.visible = false
                        bottom_horizontal_dimensions.visible = true
                        vertical_dimensions.visible = true
                    }
                    else{
                        tool.state = "option"
                        tool_origin_bot_left.visible = true
                        tool_origin_bot_right.visible = true
                    }
                }
                else{
                    handler.tool_select(group, index, orientation)
                    tool.state  = "selected"
                    top_horizontal_dimensions.visible = false
                    bottom_horizontal_dimensions.visible = true
                    vertical_dimensions.visible = true

                }
            }
            else if (group === "lower"){
                if (index === 4){

                    if (tool_options === false){
                        tool.state  = "selected"
                        top_horizontal_dimensions.visible = true
                        bottom_horizontal_dimensions.visible = false
                        vertical_dimensions.visible = true
                    }
                    else{
                        tool.state = "option"
                        tool_origin_top_left.visible = true
                        tool_origin_top_right.visible = true
                    }

                }
                else{
                    handler.tool_select(group, index, orientation)
                    tool.state  = "selected"
                    top_horizontal_dimensions.visible = true
                    bottom_horizontal_dimensions.visible = false
                    vertical_dimensions.visible = true
                }
            }
            else if (group === "right"){
                if (index === 0) {

                    if (tool_options === false){
                        tool.state  = "selected"
                        top_horizontal_dimensions.visible = true
                        bottom_horizontal_dimensions.visible = false
                        vertical_dimensions.visible = true
                    }
                    else{

                        tool.state = "option"
                        tool_origin_top_left.visible = true
                        tool_origin_top_right.visible = true
                    }

                }
                else if (index === 6) {
                    if (tool_options === false){
                        tool.state  = "selected"
                        top_horizontal_dimensions.visible = true
                        bottom_horizontal_dimensions.visible = false
                        vertical_dimensions.visible = true
                    }
                    else{
                        tool.state = "option"
                        tool_origin_bot_left.visible = true
                        tool_origin_bot_right.visible = true

                    }

                }

                else if (index < 3){
                    handler.tool_select(group, index, orientation)
                    tool.state  = "selected"
                    top_horizontal_dimensions.visible = true
                    bottom_horizontal_dimensions.visible = false
                    vertical_dimensions.visible = true

                }

                else if (index >= 3){
                    handler.tool_select(group, index, orientation)
                    tool.state  = "selected"
                    top_horizontal_dimensions.visible = false
                    bottom_horizontal_dimensions.visible = true
                    vertical_dimensions.visible = true

                }


                else{
                    handler.tool_select(group, index, orientation)
                    tool.state  = "selected"
                    top_horizontal_dimensions.visible = true
                    bottom_horizontal_dimensions.visible = false
                    vertical_dimensions.visible = false
                }
            }
        }
    }


    function choose_option(side) {

        tool_origin_top_left.visible = false
        tool_origin_top_right.visible = false

        tool_origin_bot_left.visible = false
        tool_origin_bot_right.visible = false

        var orientation = 0

        if (options.selected_group === "upper") {
            upper_tools.itemAt(options.selected_index).state = "selected"
            top_horizontal_dimensions.visible = false
            bottom_horizontal_dimensions.visible = true
            vertical_dimensions.visible = true
            if (side === "left") {
                orientation = 3
            }
            else if (side === "right"){
                orientation = 4
            }
            handler.tool_select(options.selected_group, options.selected_index, orientation)

        }
        else if (options.selected_group === "lower") {
            lower_tools.itemAt(options.selected_index).state = "selected"
            top_horizontal_dimensions.visible = true
            bottom_horizontal_dimensions.visible = false
            vertical_dimensions.visible = true
            if (side === "left") {
                orientation = 2
            }
            else if (side === "right"){
                orientation = 1
            }
            handler.tool_select(options.selected_group, options.selected_index, orientation)
        }
        else if (options.selected_group === "right") {
            right_tools.itemAt(options.selected_index).state = "selected"

            if (options.selected_index === 0) {

                top_horizontal_dimensions.visible = true
                bottom_horizontal_dimensions.visible = false
                vertical_dimensions.visible = true

                if (side === "left") {
                    orientation = 2
                }
                else if (side === "right"){
                    orientation = 1
                }
            }
            else if (options.selected_index === 6) {

                top_horizontal_dimensions.visible = false
                bottom_horizontal_dimensions.visible = true
                vertical_dimensions.visible = true

                if (side === "left") {
                    orientation = 3
                }
                else if (side === "right"){
                    orientation = 4
                }
            }

            handler.tool_select(options.selected_group, options.selected_index, orientation)
        }

    }

    Connections {
        target: handler

        onToolResetSig: {

            for (var i = 0; i < 5; i++){
                upper_tools.itemAt(i).state = "released"
                lower_tools.itemAt(i).state = "released"
            }
            for (var j = 0; j < 7; j++){
                right_tools.itemAt(j).state = "released"
            }

            top_horizontal_dimensions.visible = false
            bottom_horizontal_dimensions.visible = false
            vertical_dimensions.visible = false
        }

        onToolActiveImageSig: {
            var tool_options = false

            if (group === "lower"){
                tool_selected(lower_tools.itemAt(index), group, index, tool_options)
            }
            else if (group === "upper"){
                tool_selected(upper_tools.itemAt(index), group, index, tool_options)
            }
            else if (group === "right"){
                tool_selected(right_tools.itemAt(index), group, index, tool_options)
            }
        }
    }
}
