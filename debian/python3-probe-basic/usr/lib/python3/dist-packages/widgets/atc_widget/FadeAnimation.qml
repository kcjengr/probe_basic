//FadeAnimation.qml
import QtQuick 2.0

SequentialAnimation {
    id: root
    property QtObject target
    property string fadeProperty: "scale"
    property int fadeDuration: 150
    property alias outValue: outAnimation.to
    property alias inValue: inAnimation.to
    property alias outEasingType: outAnimation.easing.type
    property alias inEasingType: inAnimation.easing.type
    property string easingType: "Quad"
    NumberAnimation { // in the default case, fade scale to 0
        id: outAnimation
        target: root.target
        property: root.fadeProperty
        duration: root.fadeDuration
        to: 0
        easing.type: Easing["In"+root.easingType]
    }
    PropertyAction { } // actually change the property targeted by the Behavior between the 2 other animations
    NumberAnimation { // in the default case, fade scale back to 1
        id: inAnimation
        target: root.target
        property: root.fadeProperty
        duration: root.fadeDuration
        to: 1
        easing.type: Easing["Out"+root.easingType]
    }
}
