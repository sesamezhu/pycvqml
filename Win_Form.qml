import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import PyCVQML 1.0

Item {
    width: parent.width
    height: parent.height

    Timer {
        interval: 1000; running: true; repeat: true
        onTriggered: { 
            foot.text = "gpu:" + data_model.cuda +
         " 读取帧率:" + data_model.secLast +
         " 识别帧率:" + data_model.maskLast +
        }
    }
    
    CVCapture{
        id: cap_cuda1
        capType: "index"
        index: 0
        url: "c:/video/gua.MP4"
        interval: 0
        Component.onCompleted: cap_cuda1.start()
    }
    CVItem  {
        id: image_cuda1
        image: cap_cuda1.image
        width: 390
        height: 640
        desc:  "1#铁水罐左耳"
    }

}