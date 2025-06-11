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
        anchors.left: parent.left
        
        ListModel {
            id: segments_position
        }
        
        ShapePath {

            id: shapepath

            strokeWidth: 2
            strokeColor: "blue"

            fillColor: "gray"
            fillRule: ShapePath.OddEvenFill

            startX: main.width
            startY: main.height

            // Z0 at right, Z- to left, X+ up
            
            // startX: main.width + segments_position.x * 100
            // startY: main.height - segments_position.y * 100

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
        }

        Instantiator {
            id: instantiator
            model: segments_position
            onObjectAdded: shapepath.pathElements.push(object)
            PathLine {
				x: main.width + model.x * 100
                y: main.height - (model.y * 0.5) * 100
             }
        }
    }
    
    
    Connections {
        target: handler

        function onSegmentsSig(data) {
            var segment_data = JSON.parse(data);  // Deserialize the JSON data back to a dictionary

            while(segments_position.length > 0) {
                console.log("POP");
                segments_position.pop();
            }
            
            shapepath.pathElements = [];

            for (var key in segment_data) {
                if (segment_data.hasOwnProperty(key)) {

                    // console.log("Key:", key, ", Values:", segment_data[key]);

                    segments_position.append({
                         "x": parseFloat(segment_data[key][1]),  // QML X is Z
                         "y": parseFloat(segment_data[key][0])   // QML Y is X
                     })
                }
            }
        }
    }
}

