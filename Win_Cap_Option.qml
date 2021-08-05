import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.11
import QtQuick.Window 2.12

Item {
    visible: false
    x: 100
    y: 200
    width: 600
    height: 400

    Button{
        text: "重置"
        onClicked: menuAbout.onClicked()
    }
    Button{
        text:"menuQuit"
        onClicked: menuQuit.onTriggered()
    }
    
        function show(title, caption) {
            messageDialog.title = title;
            messageDialog.text = caption;
            messageDialog.open();
        }

}