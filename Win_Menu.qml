import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import PyCVQML 1.0

MenuBar {
        Menu {
            title: qsTr("文件")
            MenuItem {
                text: qsTr("打开视频")
                onTriggered: {
                    fileDialog.open()
                }
            }
            MenuItem {
                text: qsTr("退出")
                onTriggered: Qt.quit();
            }
        }

        Menu {
            title: qsTr("模式")
            MenuItem {
                id: menuCuda
                text: qsTr("GPU")
                checkable: true
                checked: data_model.cuda
            }
            Binding {
               target: data_model
               property: "cuda"
               value: menuCuda.checked
            }
            MenuItem {
                id: menuRcnn
                text: qsTr("模型")
                checkable: true
                checked: data_model.rcnn
            }
            Binding {
               target: data_model
               property: "rcnn"
               value: menuRcnn.checked
            }
            MenuItem {
                id: menuContinuous
                text: qsTr("循环")
                checkable: true
                checked: data_model.continuous
            }
            Binding {
               target: data_model
               property: "continuous"
               value: menuContinuous.checked
            }
        }
        Menu{
            title: qsTr("滤波")
            MenuItem {
                id: menuGaussian
                text: qsTr("高斯滤波")
                checkable: true
                checked: data_model.gaussian
            }
            Binding {
               target: data_model
               property: "gaussian"
               value: menuGaussian.checked
            }
            MenuItem {
                id: menuMean
                text: qsTr("均值滤波")
                checkable: true
                checked: data_model.mean
            }
            Binding {
               target: data_model
               property: "mean"
               value: menuMean.checked
            }
            MenuItem {
                id: menuHist
                text: qsTr("直方图均匀化")
                checkable: true
                checked: data_model.hist
            }
            Binding {
               target: data_model
               property: "hist"
               value: menuHist.checked
            }
            MenuItem {
                id: menuScaleUp
                text: qsTr("亮度增强")
                checkable: true
                checked: data_model.scaleUp
            }
            Binding {
               target: data_model
               property: "scaleUp"
               value: menuScaleUp.checked
            }
            MenuItem {
                id: menuScaleDown
                text: qsTr("亮度降低")
                checkable: true
                checked: data_model.scaleDown
            }
            Binding {
               target: data_model
               property: "scaleDown"
               value: menuScaleDown.checked
            }
            MenuItem {
                id: menuGray
                text: qsTr("单色")
                checkable: true
                checked: data_model.gray
            }
            Binding {
               target: data_model
               property: "gray"
               value: menuGray.checked
            }
        }
        Menu {
            title: qsTr("帮助")
            MenuItem{
                id: menuAbout
                text: qsTr("关于")
                onTriggered: messageDialog.show("安可科技", "挂钩检测")
            }
            MenuItem{
                text: "布局"
                onTriggered: caps.layoutCVItem()
            }
        }
    }