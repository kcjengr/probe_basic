import QtQuick 2.15
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.15
import QtQuick.Shapes 1.9

Rectangle {
    id: main
    visible: true
    width: 512
    height: 240
    color: "lightgray"

    Shape {
        anchors.fill: parent

        // transform: Scale{ xScale: -1; yScale: -1 }

        ListModel {
            id: segments_position;
        }

        ShapePath {
            id: shapepath
            strokeWidth: 2
            strokeColor: "blue"
            fillColor: "gray"
            fillRule: ShapePath.OddEvenFill

            startX: main.width
            startY: main.height

        }

        Instantiator {
            id: instantiator
            model: segments_position

            delegate: Loader {  // Fix: Changed from "Loader" to "Loader" (typo)
                property var modelData: model
                sourceComponent: modelData.type === "line" ? lineComponent : arcComponent

                Component {
                    id: lineComponent
                    PathLine {
                        x: modelData.x
                        y: modelData.y
                    }
                }


                Component {
                    id: arcComponent
                    PathArc {
                        property real lastX;
                        property real lastY;

                        // Get last point or start position
                        lastX: shapepath.pathElements.length > 0 ?
                                            shapepath.pathElements[shapepath.pathElements.length-1].x :
                                            shapepath.startX
                        lastY: shapepath.pathElements.length > 0 ?
                                            shapepath.pathElements[shapepath.pathElements.length-1].y :
                                            shapepath.startY

                        // Calculate chord length
                        property real chordLength: Math.sqrt(Math.pow(modelData.x - lastX, 2) +
                                                          Math.pow(modelData.y - lastY, 2))

                        // Calculate true radius for desired arc height
                        property real radiusTrue: (Math.pow(chordLength, 2) / (8 * Math.abs(modelData.r))) +
                                                (Math.abs(modelData.r) / 2)

                        // Configure arc
                        x: modelData.x
                        y: modelData.y
                        radiusX: radiusTrue
                        radiusY: radiusTrue
                        direction: modelData.r < 0 ? PathArc.Clockwise : PathArc.Counterclockwise
                    }
                }
            }

            onObjectAdded: shapepath.pathElements.push(object.item)
        }
    }

    Connections {
        target: handler

        function onSegmentsSig(data) {

            var segment_data = JSON.parse(data);
            console.log("Segments Count", segments_position.count);

            if (segments_position.count > 0) {
                segments_position.clear();
                shapepath.pathElements = [];
            }

            var moves = 0;

            for (var key in segment_data) {

                if (segment_data.hasOwnProperty(key)) {

                    var x = parseFloat(segment_data[key][0]);
                    var z = parseFloat(segment_data[key][1]);
                    var r = parseFloat(segment_data[key][2]);

                    var x_pos;
                    var z_pos;
                    var r_pos;


                    console.log("DATA X Z R = ", x, z, r);

                    if (r !== 0) {

                        x_pos = (main.height) - ((x)/2)*100;
                        z_pos = (main.width) + (z*100);
                        r_pos = r*100;


                        console.log("ARC ZX Z R", x, z, r_pos);

                        segments_position.append( {
                            "type": "arc",
                            "x": z_pos,  // origin at right, offset QML X - 10
                            "y": x_pos,  // origin at bottom, offset QML X - 5
                            "r": r_pos
                        });
                    }
                    else {

                        x_pos = (main.height) - ((x)/2)*100;
                        z_pos = (main.width) + (z*100);
                        r_pos = 0.0;

                        console.log("X Z R = ", x_pos, z_pos, r_pos);

                        //segments_position.insert(moves, {
                        segments_position.append( {
                            "type": "line",
                            "x": z_pos,  // origin at right, offset QML X - 10
                            "y": x_pos,  // origin at bottom, offset QML X - 5
                            "r": r_pos
                        });

                        console.log("OK");
                    }
                    moves ++;
                }
            }
        }
    }
}
