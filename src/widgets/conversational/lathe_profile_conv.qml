import QtQuick 2.15
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.15
import QtQuick.Shapes 1.9

Rectangle {
    id: main
    visible: true
    width: 600
    height: 300

    // Visual Properties
    property color backgroundColor: "#929695"
    property color borderColor: "white"
    property int borderWidth: 3
    property int borderRadius: 0

    // Plot line properties
    property color plotLineColor: "#000000"
    property color plotFillColor: "#4d5055"
    property color selectedColor: "#7171ED" // Color for selected segments
    property int plotLineWidth: 2
    property int selectedLineWidth: 2 // Thicker line for selected segments

    // Selection properties
    property int selectedIndex: -1 // Currently selected segment index
    property bool hasSelection: selectedIndex >= 0

    color: backgroundColor
    border.color: borderColor
    border.width: borderWidth
    radius: borderRadius

    Shape {
        id: mainShape
        anchors.fill: parent

        ListModel {
            id: segments_position;
        }
        // Main shape path
        ShapePath {
            id: shapepath
            strokeWidth: plotLineWidth
            strokeColor: plotLineColor
            fillColor: plotFillColor
            fillRule: ShapePath.OddEvenFill
            startX: main.width
            startY: main.height
        }

        // Highlight shape (always present but empty when no selection)
        Shape {
            id: highlightShape
            anchors.fill: parent

            ShapePath {
                id: selectedPath
                strokeWidth: selectedLineWidth
                strokeColor: selectedColor
                fillColor: "transparent"

                Component.onCompleted: {
                    // Start with empty path
                    pathElements = []
                }
            }
        }
        Instantiator {
            id: instantiator
            model: segments_position

            delegate: Loader {
                property var modelData: model
                property int segmentIndex: index
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
                        property real lastX: shapepath.pathElements.length > 0 ?
                                            shapepath.pathElements[shapepath.pathElements.length-1].x :
                                            shapepath.startX
                        property real lastY: shapepath.pathElements.length > 0 ?
                                            shapepath.pathElements[shapepath.pathElements.length-1].y :
                                            shapepath.startY

                        property real chordLength: Math.sqrt(Math.pow(modelData.x - lastX, 2) +
                                                Math.pow(modelData.y - lastY, 2))

                        property real radiusTrue: (Math.pow(chordLength, 2) / (8 * Math.abs(modelData.r))) +
                                                (Math.abs(modelData.r) / 2)

                        x: modelData.x
                        y: modelData.y
                        radiusX: radiusTrue
                        radiusY: radiusTrue
                        direction: modelData.r > 0 ? PathArc.Clockwise : PathArc.Counterclockwise
                    }
                }
            }

            onObjectAdded: {
                shapepath.pathElements.push(object.item)
            }
        }

        // Mouse area for selection
        MouseArea {
            anchors.fill: parent
            onClicked: {
                var closestIndex = -1
                var minDistance = Number.MAX_VALUE
                var clickPoint = Qt.point(mouse.x, mouse.y)

                // Find the closest segment to the click point
                for (var i = 0; i < segments_position.count; i++) {
                    var segment = segments_position.get(i)
                    var prevSegment = i > 0 ? segments_position.get(i-1) :
                                            {x: shapepath.startX, y: shapepath.startY}

                    var distance = distanceToSegment(
                        clickPoint,
                        Qt.point(prevSegment.x, prevSegment.y),
                        Qt.point(segment.x, segment.y)
                    )

                    if (distance < minDistance) {
                        minDistance = distance
                        closestIndex = i
                    }
                }

                // Select if within reasonable distance
                if (minDistance < 15) { // 15 pixel threshold
                    selectedIndex = closestIndex
                    updateSelectedPath()
                } else {
                    selectedIndex = -1
                    selectedPath.pathElements = []
                }
                handler.clicked(selectedIndex);
            }



            // Helper function to calculate distance from point to line segment
            function distanceToSegment(p, v, w) {
                function sqr(x) { return x * x }
                function dist2(v, w) { return sqr(v.x - w.x) + sqr(v.y - w.y) }

                var l2 = dist2(v, w)
                if (l2 === 0) return dist2(p, v)

                var t = ((p.x - v.x) * (w.x - v.x) + (p.y - v.y) * (w.y - v.y)) / l2
                t = Math.max(0, Math.min(1, t))

                return Math.sqrt(dist2(p, {
                    x: v.x + t * (w.x - v.x),
                    y: v.y + t * (w.y - v.y)
                }))
            }
        }
    }

    function updateSelectedPath() {
        selectedPath.pathElements = [] // Clear previous selection

        if (selectedIndex < 0 || selectedIndex >= segments_position.count) {
            return
        }

        var selectedSegment = segments_position.get(selectedIndex)
        var prevSegment = selectedIndex > 0 ? segments_position.get(selectedIndex-1) :
                                            {x: shapepath.startX, y: shapepath.startY}

        selectedPath.startX = prevSegment.x
        selectedPath.startY = prevSegment.y

        if (selectedSegment.type === "line") {
            var line = Qt.createQmlObject('import QtQuick 2.15; import QtQuick.Shapes 1.15; PathLine {}', selectedPath)
            line.x = selectedSegment.x
            line.y = selectedSegment.y
            selectedPath.pathElements.push(line)
        } else {
            var arc = Qt.createQmlObject('import QtQuick 2.15; import QtQuick.Shapes 1.15; PathArc {}', selectedPath)
            arc.x = selectedSegment.x
            arc.y = selectedSegment.y

            var chordLength = Math.sqrt(Math.pow(selectedSegment.x - prevSegment.x, 2) +
                                     Math.pow(selectedSegment.y - prevSegment.y, 2))
            var radiusTrue = (Math.pow(chordLength, 2) / (8 * Math.abs(selectedSegment.r))) +
                           (Math.abs(selectedSegment.r) / 2)

            arc.radiusX = radiusTrue
            arc.radiusY = radiusTrue
            arc.direction = selectedSegment.r > 0 ? PathArc.Clockwise : PathArc.Counterclockwise

            selectedPath.pathElements.push(arc)
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
        // Z maps to screen width (600), X maps to screen height (300)
        var availableWidth = main.width * 0.9;   // 80% of width for Z axis
        var availableHeight = main.height * 0.6; // 80% of height for X axis

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

        function onSelectedSig(index) {
            console.log("Segments Active row", index);
            selectedIndex = index;
            updateSelectedPath();
        }

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
