import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.11
import QtQuick.Window 2.12

ApplicationWindow {
    visible: true
    width: 1024
    height: 800
    title: qsTr("炼钢厂天车挂钩检测系统")
    background: Image {
        source: "background.png"
    }

    menuBar:Loader{
        source:"Test_Menu.qml"
    }
    
    Button{
        text:"winCapOption.showshowshowshowshowshow"
        onClicked:winCapOption.show("winCapOption","show")
    }
    
    Win_Cap_Option{id:"winCapOption"}

    footer: Label {
        id: foot
        font.bold: true
        font.pointSize: 14
        text: qsTr("gpu: 循环:")
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
