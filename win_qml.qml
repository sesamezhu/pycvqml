import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.11
import QtQuick.Window 2.12
import PyCVQML 1.0

ApplicationWindow {
    visible: true
    width: 1024
    height: 800
    title: qsTr("炼钢厂天车挂钩检测系统")
    background: Image {
        source: "background.png"
    }

    CVAction {
        id: cvAction
    }

    FileDialog {
        id: fileDialog
        nameFilters: ["MP4 files (*.mp4)", "All Files (*.*)"]
        onAccepted: {
            try{
                cvAction.play(fileUrl)
            } catch (error){
                        messageDialog.title = "Error play " + fileUrl 
                        messageDialog.text = error.toString()
                        messageDialog.icon = StandardIcon.Critical
                        messageDialog.open()
            }
        }
    }

    menuBar: Loader{
        source: "Win_Menu.qml"
    }


    Item {
        id: caps
        anchors.fill: parent
        Timer {
            interval: 1000; running: true; repeat: true
            onTriggered: { 
                foot.text = "gpu:" + data_model.cuda +
             " 读取帧率:" + data_model.secLast +
             " 识别帧率:" + data_model.maskLast
            }
        }
        
        CVCapture{
            id: cap_cuda1
            url: "rtsp://admin:oalb1234@192.168.13.202:554/Streaming/Channels/1"
            Component.onCompleted: cap_cuda1.start()
        }
        CVItem  {
            id: image_cuda1
            image: cap_cuda1.image
            desc:  "1#铁水罐左耳"
        }
        
        CVCapture{
            id: cap_cuda2
            url: "rtsp://admin:oalb1234@192.168.13.202:554/Streaming/Channels/1"
            Component.onCompleted: cap_cuda2.start()
        }
        CVItem  {
            id: image_cuda2
            image: cap_cuda2.image
            desc:  "1#铁水罐右耳"
            Text {
                text:parent.desc
                anchors.left:parent.left
                anchors.top:parent.top
                
            }
        }
        
        CVCapture{
            id: cap_cuda3
            url: "rtsp://admin:oalb1234@192.168.13.202:554/Streaming/Channels/1"
            Component.onCompleted: cap_cuda3.start()
        }
        CVItem  {
            id: image_cuda3
            image: cap_cuda3.image
            desc:  "2#铁水罐左耳"
        }
        
        CVCapture{
            id: cap_cuda4
            url: "rtsp://admin:oalb1234@192.168.13.202:554/Streaming/Channels/1"
            Component.onCompleted: cap_cuda4.start()
        }
        CVItem  {
            id: image_cuda4
            image: cap_cuda4.image
            desc:  "2#铁水罐右耳"
        }
        
        Component.onCompleted: caps.layoutCVItem()
        
        function layoutCVItem() {
            var wid = caps.width / 2 - 20
            var high = caps.height / 2 - 5
            image_cuda1.x = 20
            image_cuda1.y = 0
            image_cuda1.width = wid
            image_cuda1.height = high
            image_cuda2.x = 20 + wid
            image_cuda2.y = 0
            image_cuda2.width = wid
            image_cuda2.height = high
            image_cuda3.x = 20
            image_cuda3.y = 10 + high
            image_cuda3.width = wid
            image_cuda3.height = high
            image_cuda4.x = 20 + wid
            image_cuda4.y = 10 + high
            image_cuda4.width = wid
            image_cuda4.height = high
        }
    }


    footer: Label {
        id: foot
        font.bold: true
        font.pointSize: 14
        text: qsTr("gpu:" + data_model.cuda + " 循环:" + data_model.continuous)
        color: "#ffffff"
    }

    MessageDialog {
        id: messageDialog

        function show(title, caption) {
            messageDialog.title = title;
            messageDialog.text = caption;
            messageDialog.open();
        }
    }

}
