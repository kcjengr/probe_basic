import QtQuick 2.15
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.15
import QtQuick.Shapes 1.9

Rectangle {
    id: main
    visible: true
    width: 800
    height: 400
    
    // Visual Properties - QML compatible color formats
    property color backgroundColor: "#929695"  // Hex format
    property color borderColor: "darkgrey"      // Hex for darkgray
    property int borderWidth: 3
    property int borderRadius: 0
    
    // Plot line properties
    property color plotLineColor: "#2F303C"   // Hex for blue
    property color plotFillColor: "#2F303C"    // Hex for darkgray
    property int plotLineWidth: 3
    
    color: backgroundColor
    border.color: borderColor
    border.width: borderWidth
    radius: borderRadius

    Shape {
        anchors.fill: parent

        // transform: Scale{ xScale: -1; yScale: -1 }

        ListModel {
            id: segments_position;
        }

        ShapePath {
            id: shapepath
            strokeWidth: plotLineWidth
            strokeColor: plotLineColor
            fillColor: plotFillColor
            fillRule: ShapePath.OddEvenFill

            startX: main.width
            startY: main.height
        }

        Instantiator {
            id: instantiator
            model: segments_position

            delegate: Loader {
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
                        direction: modelData.r > 0 ? PathArc.Clockwise : PathArc.Counterclockwise
                    }
                }
            }

            onObjectAdded: shapepath.pathElements.push(object.item)
        }
    }

    // Simple function to calculate dynamic scale factor only
    function calculateScale(segment_data) {
        var minX = Number.MAX_VALUE;
        var maxX = Number.MIN_VALUE;
        var minZ = Number.MAX_VALUE;
        var maxZ = Number.MIN_VALUE;
        var hasData = false;

        // Find bounds
        for (var key in segment_data) {
            if (segment_data.hasOwnProperty(key)) {
                var x = parseFloat(segment_data[key][0]);
                var z = parseFloat(segment_data[key][1]);

                if (!isNaN(x) && !isNaN(z)) {
                    minX = Math.min(minX, x);
                    maxX = Math.max(maxX, x);
                    minZ = Math.min(minZ, z);
                    maxZ = Math.max(maxZ, z);
                    hasData = true;
                }
            }
        }

        if (!hasData) {
            return 100; // Default scale
        }

        var xRange = Math.abs(maxX - minX);
        var zRange = Math.abs(maxZ - minZ);

        // Ensure minimum range for very small parts
        if (xRange < 0.1) xRange = 0.1;
        if (zRange < 0.1) zRange = 0.1;

        // Account for the /2 division in the X coordinate transformation
        var effectiveXRange = xRange / 2;  // This matches the actual plotting transformation

        // Calculate scale based on actual axis usage
        // Z maps to screen width (800), X maps to screen height (400)
        var availableWidth = main.width * 0.8;   // 80% of width for Z axis
        var availableHeight = main.height * 0.8; // 80% of height for X axis
        
        var scaleForZ = availableWidth / zRange;        // Scale to fit Z range in width
        var scaleForX = availableHeight / effectiveXRange; // Scale to fit effective X range in height
        
        // Use the smaller scale to maintain aspect ratio
        var scale = Math.min(scaleForZ, scaleForX);

        // Reasonable scale limits
        scale = Math.max(10, Math.min(scale, 1000));

        console.log("Dynamic scale calculated:", scale, "X range:", xRange, "effective X range:", effectiveXRange, "Z range:", zRange, "scaleForX:", scaleForX, "scaleForZ:", scaleForZ);
        return scale;
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

            // Calculate dynamic scale factor
            var dynamicScale = calculateScale(segment_data);

            var moves = 0;
            var firstZ = null;
            var lastZ = null;

            for (var key in segment_data) {

                if (segment_data.hasOwnProperty(key)) {

                    var x = parseFloat(segment_data[key][0]);
                    var z = parseFloat(segment_data[key][1]);
                    var r = parseFloat(segment_data[key][2]);

                    var x_pos;
                    var z_pos;
                    var r_pos;

                    // Track first and last Z positions for proper fill closure
                    if (firstZ === null) firstZ = z;
                    lastZ = z;

                    console.log("DATA X Z R = ", x, z, r);

                    if (r !== 0) {

                        // Apply dynamic scale to existing calculation
                        x_pos = (main.height) - ((x)/2)*dynamicScale;
                        z_pos = (main.width) + (z*dynamicScale);
                        r_pos = (r*2) * dynamicScale;

                        console.log("ARC ZX Z R", x, z, r_pos);

                        segments_position.append( {
                            "type": "arc",
                            "x": z_pos,  // origin at right, offset QML X - 10
                            "y": x_pos,  // origin at bottom, offset QML X - 5
                            "r": r_pos
                        });
                    }
                    else {

                        // Apply dynamic scale to existing calculation
                        x_pos = (main.height) - ((x)/2)*dynamicScale;
                        z_pos = (main.width) + (z*dynamicScale);
                        r_pos = 0.0;

                        console.log("X Z R = ", x_pos, z_pos, r_pos);

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

            // Close the path properly for lathe profile fill
            if (moves > 0) {
                // Add line to centerline at end of profile
                var centerlineY = main.height; // X=0 centerline position
                var endZ = (main.width) + (lastZ*dynamicScale);
                
                segments_position.append({
                    "type": "line",
                    "x": endZ,
                    "y": centerlineY,
                    "r": 0.0
                });

                // Add line along centerline back to start
                var startZ = (main.width) + (firstZ*dynamicScale);
                
                segments_position.append({
                    "type": "line", 
                    "x": startZ,
                    "y": centerlineY,
                    "r": 0.0
                });
            }
        }
    }
}
