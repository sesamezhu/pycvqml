import PyCVQML 1.0
import Filters 1.0
import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Item {
    width: 1024
    height: 768
    Image {
        id: top_image
        width: window.width
        height: window.height
        source: "../background.png"
        fillMode: Image.Tile
    }

    CVCapture{
        id: cap_cuda
        capType: "cuda"
        url: "/video/6969012508999466304.MP4"
        interval: 10
        Component.onCompleted: cap_cuda.start()
    }
    CVItem  {
        id: image_cuda
        image: cap_cuda.image
        x: 20
        y: 200
        width: 320
        height: 640
    }
    Label {
        id: label1
        x: 15
        y: 140
        text: qsTr("检测点1")
        color: "#ffffff"
        font.bold: true
        font.pointSize: 16
        font.family: "Arial"
    }

    CVCapture{
        id: cap_url
        capType: "url"
        url: "/video/6969012508999466304.MP4"
        interval: 10
        Component.onCompleted: cap_url.start()
    }
    CVItem  {
        id: image_url
        image: cap_url.image
        x: 420
        y: 200
        width: 320
        height: 640
    }
    Label {
        id: label_url
        x: 415
        y: 140
        text: qsTr("检测点url")
        color: "#ffffff"
        font.bold: true
        font.pointSize: 16
        font.family: "Arial"
    }


    MaxRGBFilter{
        id: max_rgb_filter
    }
    GrayFilter{
        id: gray_filter
    }
}