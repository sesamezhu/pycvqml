import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.11
import QtQuick.Window 2.12

MenuBar {
        id: innerMenuBar
        Menu {
            title: qsTr("文件")
            MenuItem {
                id: menuQuit
                text: qsTr("退出")
                onTriggered: Qt.quit();
            }
        }

        Menu {
            title: qsTr("帮助")
            MenuItem{
                id: menuAbout
                text: qsTr("关于")
                onTriggered: messageDialog.show("安可科技", "挂钩检测")
            }
        }
    }