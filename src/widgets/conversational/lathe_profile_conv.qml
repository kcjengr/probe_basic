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


    property real t0: 0.0
    property real t1: 0.0
    property real t2: 0.0

    property real t3: 0.0
    property real t4: 0.0
    property real t5: 0.0

    property real t6: 0.0
    property real t7: 0.0
    property real t8: 0.0

    property real t9: 0.0
    property real t10: 0.0
    property real t11: 0.0

    property real t12: 0.0
    property real t13: 0.0
    property real t14: 0.0

    property real t15: 0.0
    property real t16: 0.0
    property real t17: 0.0


    Shape {
        anchors.left: parent.left

        ShapePath {

            id: shapepath

            strokeWidth: 2
            strokeColor: "blue"

            fillColor: "gray"
            fillRule: ShapePath.OddEvenFill

            startX: main.width
            startY: main.height


//            PathLine { relativeX: -main.t0; relativeY: -main.t1 }
//            PathLine { relativeX: -main.t3; relativeY: -main.t4 }
//            PathLine { relativeX: -main.t6; relativeY: -main.t7 }
//            PathLine { relativeX: -main.t9; relativeY: -main.t10 }
//            PathLine { relativeX: -main.t12; relativeY: -main.t13 }
//            PathLine { relativeX: -main.t15; relativeY: -main.t16 }

            PathLine { x: main.width + main.t0; y: main.height - main.t1 }
            PathLine { x: main.width + main.t3; y: main.height - main.t4 }
            PathLine { x: main.width + main.t6; y: main.height - main.t7 }
            PathLine { x: main.width + main.t9; y: main.height - main.t10 }
            PathLine { x: main.width + main.t12; y: main.height - main.t13 }
            PathLine { x: main.width + main.t15; y: main.height - main.t16 }

     //       PathLine { x: main.width + main.t15; y: main.heigh }

//            PathLine { x: 0; y: main.t16 }
//            PathLine { x: 0; y: main.height }
//            PathLine { x: main.width; y: main.height }


//            PathArc {
//                relativeX: 150; y: 250
//                radiusX: 300; radiusY: 300
//            }

//            PathArc {
//              relativeX: 400;
//              relativeY: 30;

//              radiusX: 6;
//              radiusY: 6;
//              useLargeArc: true;
//              direction: PathArc.CloclkWise }


//            PathAngleArc {
//                relativeX: 200
//                y: -100
//                startAngle: 22.5
//            }


//            PathArc {
//                relativeX: 50; y: -100
//                radiusX: 25; radiusY: 25
//            }
//            PathArc {
//                relativeX: 50; y: -100
//                radiusX: 25; radiusY: 50
//            }
//            PathArc {
//                relativeX: 50; y: -100
//                radiusX: 50; radiusY: -100
//            }

            // The circle

//            PathArc { x: 0; y: 100; radiusX: 10; radiusY: 100; useLargeArc: true }

//            PathLine { x: 40; y: 120 }

//            PathArc { x: -40; y: 120; radiusX: 120; radiusY: 120; useLargeArc: true; direction: PathArc.Counterclockwise }

//            PathLine { x: -40; y: 200 }

            // The dots

            //PathMove { x: -20; y: 80 }

            // PathArc { x: 20; y: 80; radiusX: 20; radiusY: 20; useLargeArc: true }
            // PathArc { x: -20; y: 80; radiusX: 20; radiusY: 20; useLargeArc: true }

            // //PathMove { x: -20; y: 130 }
            // PathArc { x: 20; y: 130; radiusX: 20; radiusY: 20; useLargeArc: true }
            // PathArc { x: -20; y: 130; radiusX: 20; radiusY: 20; useLargeArc: true }

            //PathMove { x: -20; y: 180 }
            // PathArc { x: 20; y: 180; radiusX: 20; radiusY: 20; useLargeArc: true }
            // PathArc { x: -20; y: 180; radiusX: 20; radiusY: 20; useLargeArc: true }

            //PathMove { x: -20; y: 230 }
            //º PathArc { x: 20; y: 230; radiusX: 20; radiusY: 20; useLargeArc: true }
            // PathArc { x: -20; y: 230; radiusX: 20; radiusY: 20; useLargeArc: true }

        }
    }
    Connections {
        target: handler

        function onSegmentsSig(data) {
            var segment_data = JSON.parse(data);  // Deserialize the JSON data back to a dictionary
            for (var key in segment_data) {
                if (segment_data.hasOwnProperty(key)) {
//                     console.log("Key:", key, ", Values:", segment_data  [key]);

                    t0 = parseFloat(segment_data[0][1]);
                    t1 = parseFloat(segment_data[0][0]);
                    t2 = parseFloat(segment_data[0][2]);

                    t3 = parseFloat(segment_data[1][1]);
                    t4 = parseFloat(segment_data[1][0]);
                    t5 = parseFloat(segment_data[1][2]);

                    t6 = parseFloat(segment_data[2][1]);
                    t7 = parseFloat(segment_data[2][0]);
                    t8 = parseFloat(segment_data[2][2]);

                    t9 = parseFloat(segment_data[3][1]);
                    t10 = parseFloat(segment_data[3][0]);
                    t11 = parseFloat(segment_data[3][2]);

                    t12 = parseFloat(segment_data[4][1]);
                    t13 = parseFloat(segment_data[4][0]);
                    t14 = parseFloat(segment_data[4][2]);

                    t15 = parseFloat(segment_data[5][1]);
                    t16 = parseFloat(segment_data[5][0]);
                    t17 = parseFloat(segment_data[5][2]);


                }
            }
        }

    }
}
