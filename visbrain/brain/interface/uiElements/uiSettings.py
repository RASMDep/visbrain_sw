# -*- coding: utf-8 -*-

"""Main class for settings managment (save / load / light / cameras...)."""
import os
import numpy as np
from PyQt4.QtGui import *
from PyQt4 import QtCore


from vispy import io
import vispy.scene.cameras as viscam

from ....utils import uiSpinValue

__all__ = ['uiSettings']


class uiSettings(object):
    """Main class for settings managment (save / load / light / cameras...)."""

    def __init__(self):
        """Init."""
        # =============================================================
        # MENU & FILES
        # =============================================================
        self.progressBar.hide()

        # ------------- Screenshot / Exit -------------
        self.actionScreenshot.triggered.connect(self._screenshot)
        self.actionExit.triggered.connect(qApp.quit)

        # ------------- Display -------------
        self.actionUi_settings.triggered.connect(self._fcn_panSettingsViz)
        self.actionMNI.triggered.connect(self._fcn_panSettingsViz)
        self.actionSources.triggered.connect(self._fcn_panSettingsViz)
        self.actionConnectivity.triggered.connect(self._fcn_panSettingsViz)
        self.actionColormap.triggered.connect(self._fcn_panSettingsViz)

        # ------------- Transform -------------
        self.actionProjection.triggered.connect(self._fcn_menuProjection)
        self.actionRepartition.triggered.connect(self._fcn_menuRepartition)

        # ------------- Help -------------
        self.actionShortcut.triggered.connect(self._fcn_showShortPopup)
        self.actionDocumentation.triggered.connect(self._fcn_openDoc)

        # =============================================================
        # SCREENSHOT
        # =============================================================
        # Set values :
        self._ssResolution.setValue(self._uirez)
        self._ssSaveAs.setPlaceholderText("myfile")
        if self._crop is not None:
            self._ssCropXs.setValue(self._crop[0])
            self._ssCropYs.setValue(self._crop[1])
            self._ssCropXe.setValue(self._crop[2])
            self._ssCropYe.setValue(self._crop[2])
        # Connections :
        self._ssSaveAs.editingFinished.connect(self._screenshotSettings)
        self._ssSaveAsExt.currentIndexChanged.connect(self._screenshotSettings)
        self._ssCropEnable.clicked.connect(self._screenshotSettings)
        self._ssResolution.valueChanged.connect(self._screenshotSettings)
        self._ssCbEnable.clicked.connect(self._screenshotSettings)
        self._ssRun.clicked.connect(self._fcn_runScreenshot)
        self._ssGuide.clicked.connect(self._screenshotSettings)
        self._ssCropXs.valueChanged.connect(self._screenshotSettings)
        self._ssCropYs.valueChanged.connect(self._screenshotSettings)
        self._ssCropXe.valueChanged.connect(self._screenshotSettings)
        self._ssCropYe.valueChanged.connect(self._screenshotSettings)

        # =============================================================
        # SETTINGS PANEL
        # =============================================================
        # Quick settings panel :
        self.actionQuick_settings.triggered.connect(self._toggle_settings)
        self.QuickSettings.currentChanged.connect(self._fcn_onTabChange)
        self.q_widget.setVisible(True)

        # Background color :
        self.bgd_green.valueChanged.connect(self._fcn_bgd_color)
        self.bgd_red.valueChanged.connect(self._fcn_bgd_color)
        self.bgd_blue.valueChanged.connect(self._fcn_bgd_color)

        # =============================================================
        # ROTATION
        # =============================================================
        # Coronal / axial / sagittal :
        self.q_coronal.clicked.connect(self._fcn_coronal)
        self.q_axial.clicked.connect(self._fcn_axial)
        self.q_sagittal.clicked.connect(self._fcn_sagittal)

        # =============================================================
        # LIGHT
        # =============================================================
        # Position :
        self.uil_posX.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_posY.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_posZ.valueChanged.connect(self._light_Ui2Atlas)
        # Intensity :
        self.uil_intX.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_intY.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_intZ.valueChanged.connect(self._light_Ui2Atlas)
        # Color :
        self.uil_colR.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_colG.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_colB.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_colA.valueChanged.connect(self._light_Ui2Atlas)
        # Coeffient :
        self.uil_AmbCoef.valueChanged.connect(self._light_Ui2Atlas)
        self.uil_SpecCoef.valueChanged.connect(self._light_Ui2Atlas)

        self._light_Atlas2Ui()

        # =============================================================
        # CAMERAS
        # =============================================================
        # Cameras types :
        self.c_Turnable.clicked.connect(self._fcn_switch_camera)
        self.c_Fly.clicked.connect(self._fcn_switch_camera)

        # =============================================================
        # ERROR // WARNING MESSAGES
        # =============================================================
        # Hide Error / warning wessage :
        self.UserMsgBox.setVisible(False)
        # Hide rotation panel :
        self.userRotationPanel.setVisible(False)

    # =============================================================
    # MENU & FILE MANAGMENT
    # =============================================================
    def _fcn_showShortPopup(self):
        """Open shortcut window."""
        self._shpopup.show()

    def _fcn_openDoc(self):
        """Open documentation."""
        import webbrowser
        webbrowser.open('http://etiennecmb.github.io/visbrain/brain.html')

    def _fcn_panSettingsViz(self):
        """
        """
        # Ui settings :
        if self.actionUi_settings.isChecked():
            self.QuickSettings.setCurrentIndex(0)
            self.q_widget.setVisible(True)
            self.actionUi_settings.setChecked(False)
        elif self.actionMNI.isChecked():
            self.QuickSettings.setCurrentIndex(1)
            self.q_widget.setVisible(True)
            self.actionMNI.setChecked(False)
        elif self.actionSources.isChecked():
            self.QuickSettings.setCurrentIndex(2)
            self.q_widget.setVisible(True)
            self.actionSources.setChecked(False)
        elif self.actionConnectivity.isChecked():
            self.QuickSettings.setCurrentIndex(3)
            self.q_widget.setVisible(True)
            self.actionConnectivity.setChecked(False)
        elif self.actionColormap.isChecked():
            self.QuickSettings.setCurrentIndex(4)
            self.q_widget.setVisible(True)
            self.actionColormap.setChecked(False)

    # =============================================================
    # SCREENSHOT
    # =============================================================
    def _fcn_runScreenshot(self):
        """Run the screenshot."""
        # Get latest settings :
        self._screenshotSettings()
        # Run screenshot :
        self._screenshot()

    def _screenshotSettings(self):
        """Get screenshot settings from the GUI.s"""
        # ------------- MAIN CANVAS -------------
        # Get filename :
        file = str(self._ssSaveAs.text())
        ext = str(self._ssSaveAsExt.currentText())
        self._savename = file + ext
        # Cropping :
        viz = self._ssCropEnable.isChecked()
        crop = (self._ssCropXs.value(), self._ssCropYs.value(),
                self._ssCropXe.value(), self._ssCropYe.value())
        self._crop = crop if viz else None
        self._ssCropW.setEnabled(viz)
        # self.guide.mesh.visible = self._ssGuide.isChecked()
        # if self._ssGuide.isChecked() and self._ssCropW.isEnabled():
        #     print(self.view.wc.camera.center)
        #     self.guide.size = self.view.canvas.size
        #     self.guide.range['x'] = self.view.wc.camera._xlim
        #     self.guide.range['y'] = self.view.wc.camera._ylim
        #     print(self.guide.range)
        #     self.guide.set_data(crop=crop)
        # Resolution :
        self._uirez = float(self._ssResolution.value())

        # ------------- COLORBAR CANVAS -------------
        # Colorbar :
        viz = self._ssCbEnable.isChecked()
        self._qcmapVisible.setChecked(viz)
        self._toggle_cmap()
        self.cb['export'] = viz

    def _screenshot(self):
        """Screenshot using the GUI.

        This function need that a savename is already defined (otherwise, a
        window appeared so that the user specify the path/name). Then, it needs
        an extension (png) and a boolean parameter (self.cb['export']) to
        specify if the colorbar has to be exported.
        """
        # Manage filename :
        if isinstance(self._savename, str):
            cond = self._savename.split('.')[0] == ''
        if (self._savename is None) or cond:
            saveas = str(QFileDialog.getSaveFileName(self, 'Save screenshot',
                                                     os.getenv('HOME')))
        else:
            saveas = self._savename

        # Get filename and extension :
        file, ext = os.path.splitext(saveas)
        if not ext:
            raise ValueError("No extension detected in "+saveas)

        # Manage size exportation. The dpi option present when creating a
        # vispy canvas doesn't seems to work. The trick bellow increase the
        # physical size of the canvas so that the exported figure has a
        # high-definition :
        # Get a copy of the actual canvas physical size :
        backp_size = self.view.canvas.physical_size

        # Increase the physical size :
        ratio = max((2*self._uirez)/backp_size[0], self._uirez/backp_size[1])
        new_size = (int(backp_size[0]*ratio), int(backp_size[1]*ratio))
        self.view.canvas._backend._physical_size = new_size

        # Render and save :
        if self._crop is not None:
            kwargs = {'region': self._crop}
        else:
            kwargs = {'size': new_size}
        img = self.view.canvas.render(**kwargs)
        io.imsave(saveas, img)

        # Set to the canvas it's previous size :
        self.view.canvas._backend._physical_size = backp_size

        # Export the colorbar :
        # self.cb['export'] = True
        if self.cb['export']:
            # Get a copy of the actual canvas physical size :
            backp_size = self.view.cbcanvas.physical_size
            new_size = (int(backp_size[0]*ratio), int(backp_size[1]*ratio))
            self.view.cbcanvas._backend._physical_size = new_size
            # Render colorbar panel :
            if self._crop is not None:
                kwargs = {'region': self._cbcrop}
            else:
                kwargs = {'size': new_size}
            cbimg = self.view.cbcanvas.render(**kwargs)
            # Colorbar file name : filename_colorbar.extension
            filename = saveas.replace('.', '_colorbar.')
            io.imsave(filename, cbimg)
            # Set to the canvas it's previous size :
            self.view.cbcanvas._backend._physical_size = backp_size

    def _toggle_settings(self):
        """Toggle method for display / hide the settings panel."""
        viz = self.q_widget.isVisible()
        self.q_widget.setVisible(not viz)
        self._xyzRange['turntable']['x'] = (-950, 1050) if viz else (-750, 850)

    def _fcn_bgd_color(self):
        """Change canvas background color."""
        bgd = (self.bgd_red.value(), self.bgd_green.value(),
               self.bgd_blue.value())
        self.view.canvas.bgcolor = bgd
        self.view.cbcanvas.bgcolor = bgd

    def _fcn_onTabChange(self):
        """Triggered method when tab changed."""
        # Get current tab :
        currentIndex = self.QuickSettings.currentIndex()
        if currentIndex == 2:
            self.cmapSources.setChecked(True)
        if currentIndex == 3:
            self.cmapConnect.setChecked(True)
        self._select_object_cmap()

    def _fcn_menuProjection(self):
        """Run the cortical projection."""
        self._tprojectas = 'activity'
        self._sourcesProjection()

    def _fcn_menuRepartition(self):
        """Run the cortical projection."""
        self._tprojectas = 'repartition'
        self._sourcesProjection()

    # =============================================================
    # ROTATION
    # =============================================================
    def _rotate(self, fixed=None, custom=None):
        """Rotate the scene elements using a predefined or a custom rotation.

        The rotation is applied on every objects on the scene.

        Kargs:
            fixed: string, optional, (def: 'axial')
                Predefined rotation. Use either 'axial', 'coronal' or
                'sagittal'. As a complement, use the suffixe '_0' or
                '_1' to switch between possible views.
                    * 'axial_0/1': switch between top/bottom view
                    * 'coronal_0/1': switch between front/back view
                    * 'sagittal_0/1': switch between left/right view

            custom: tuple, optional, (def: None)
                Custom rotation. The custom parameter must be a
                tuple of two float respectively for azimuth and
                elevation.
        """
        # Check the fixed parameter :
        if fixed is not None:
            if not isinstance(fixed, str) or not any([bool(fixed.find(
                            k)+1) for k in ['axial', 'sagittal', 'coronal']]):
                raise ValueError("fixed must contain 'axial', 'coronal' or "
                                 "'sagittal")
            else:
                if bool(fixed.find('_')+1):
                    view, side = tuple(fixed.split('_'))
                    exec('self.atlas.' + view + ' = ' + side)
                else:
                    view, side = fixed, None
        else:
            view, side = None, None
        # Check the custom parameter :
        if custom is not None:
            if not isinstance(custom, (tuple, list)) or len(custom) is not 2:
                raise ValueError("The custom parameter must be a tuple of "
                                 "two floats (azimuth, elevation)")

        azimuth, elevation = 0, 90
        if view is not None:
            # Sagittal (left, right)
            if view == 'sagittal':
                if self.atlas.sagittal == 0:  # Left
                    azimuth, elevation = -90, 0
                    self.atlas.sagittal = 1
                elif self.atlas.sagittal == 1:  # Right
                    azimuth, elevation = 90, 0
                    self.atlas.sagittal = 0
                self.atlas.coronal, self.atlas.axial = 0, 0
            # Coronal (front, back)
            elif view == 'coronal':
                if self.atlas.coronal == 0:  # Front
                    azimuth, elevation = 180, 0
                    self.atlas.coronal = 1
                elif self.atlas.coronal == 1:  # Back
                    azimuth, elevation = 0, 0
                    self.atlas.coronal = 0
                self.atlas.sagittal, self.atlas.axial = 0, 0
            # Axial (top, bottom)
            elif view == 'axial':
                if self.atlas.axial == 0:  # Top
                    azimuth, elevation = 0, 90
                    self.atlas.axial = 1
                elif self.atlas.axial == 1:  # Bottom
                    azimuth, elevation = 0, -90
                    self.atlas.axial = 0
                self.atlas.sagittal, self.atlas.coronal = 0, 0
        elif custom is not None:
            azimuth, elevation = custom[0], custom[1]

        # Set camera and range :
        self.view.wc.camera.azimuth = azimuth
        self.view.wc.camera.elevation = elevation
        self._set_cam_range()

    def _set_cam_range(self, name='turntable'):
        """Set the camera range."""
        dic = self._xyzRange[name]
        self.view.wc.camera.set_range(x=dic['x'], y=dic['x'], z=dic['z'])

    def _fcn_coronal(self):
        """GUI to deep function for a fixed coronal view."""
        self._rotate(fixed='coronal')

    def _fcn_axial(self):
        """GUI to deep function for a fixed axial view."""
        self._rotate(fixed='axial')

    def _fcn_sagittal(self):
        """GUI to deep function for a fixed sagittal view."""
        self._rotate(fixed='sagittal')

    # =============================================================
    # LIGHT
    # =============================================================
    def _light_Ui2Atlas(self):
        """Get light properties from the GUI and set it to the atlas.

        This function get light position / Intensity / Color / Coefficients
        from the graphical user interface and set it to the atlas.
        """
        # Position :
        l_pos = (self.uil_posX.value(), self.uil_posY.value(),
                 self.uil_posZ.value())
        # Intensity :
        l_int = (self.uil_intX.value(), self.uil_intY.value(),
                 self.uil_intZ.value())
        # Color :
        l_col = (self.uil_colR.value(), self.uil_colG.value(),
                 self.uil_colB.value(), self.uil_colA.value())
        # Coef :
        l_amb, l_spec = self.uil_AmbCoef.value(), self.uil_SpecCoef.value()

        self.atlas.mesh.set_light(l_position=l_pos, l_color=l_col,
                                  l_intensity=l_int, l_coefAmbient=l_amb,
                                  l_coefSpecular=l_spec)

    def _light_Atlas2Ui(self):
        """Get light properties from the atlas and set it to the GUI.

        This function get light position / Intensity / Color / Coefficients
        from the atlas and set it to the graphical user interface.
        """
        uiSpinValue([self.uil_posX, self.uil_posY, self.uil_posZ,
                     self.uil_intX, self.uil_intY, self.uil_intZ,
                     self.uil_colR, self.uil_colG, self.uil_colB,
                     self.uil_colA, self.uil_AmbCoef, self.uil_SpecCoef],
                    self.atlas.mesh.get_light)

    # =============================================================
    # CAMERA
    # =============================================================
    def _fcn_switch_camera(self):
        """Switch between different types of cameras.

        The user can either use a Turntable or a Fly camera. The turntable
        camera is centered on the central object. Every rotation is arround
        this object. The fly camera can be used for go in every deep part of
        the brain (not easy to control).
        """
        # Get radio buttons values :
        if self.c_Turnable.isChecked():
            camera = viscam.TurntableCamera(azimuth=0, distance=1000,
                                            name='turntable')
        if self.c_Fly.isChecked():
            # camera = viscam.PanZoomCamera(aspect=1)
            camera = viscam.FlyCamera(name='fly')

        # Add camera to the mesh and to the canvas :
        self.view.wc.camera = camera
        self.atlas.mesh.set_camera(camera)
        if self.area.name == 'displayed':
            self.area.mesh.set_camera(camera)
        self.view.wc.update()
        self._set_cam_range(name=camera.name)

    # =============================================================
    # ERROR // WARNING MESSAGES
    # =============================================================
    def _userMsg(self, message, kind='error', during=10, fontsize=9):
        """Display error / warning message to the user.

        This method display an error / warning message for the user. This
        message is displayed at the bottom of the settings panel.

        Args:
            message: str
                The message to displayed.

        Kargs:
            kind: str, optional, (def: 'error')
                The type of message to display. Use either 'error' (for a red
                bold error message) or 'warn' (for a blue message.)

            during: float, optional, (def: 10.0)
                The duration of the message. After this delay, the message
                disapear.

            fontsize: int, optional, (def: 9)
                The fontsize of the displayed message.
        """
        # Only display this message if there's no already present message :
        if not self.UserMsgBox.isVisible():
            # Set settings panel visible :
            self.q_widget.setVisible(True)

            # Set the widget and the error message visible :
            self.UserMsgBox.setVisible(True)
            self.uiErrorMsg.setVisible(True)

            # Change the color depending on warning / error type :
            palette = QPalette()
            palette.setColor(QPalette.Background, QtCore.Qt.white)
            # Error type :
            if kind is 'error':
                message = 'ERROR:\n' + message
                palette.setColor(QPalette.Foreground, QtCore.Qt.red)
            # Warning type :
            elif kind is 'warn':
                message = 'Warning:\n' + message
                palette.setColor(QPalette.Foreground, QtCore.Qt.blue)
            else:
                raise ValueError("Choose either between 'error' or 'warn'.")

            # Set message text and color:
            self.uiErrorMsg.setText(message)
            self.uiErrorMsg.setAutoFillBackground(True)
            self.uiErrorMsg.setPalette(palette)
            self.uiErrorMsg.setFont(QFont("Times", fontsize, QFont.Bold))

            # Message disappear :
            def _delayedMsg():
                self.UserMsgBox.setVisible(False)
                self.uiErrorMsg.setVisible(False)

            # Set a pyqt timer to delayed when the message is hide :
            timer = QtCore.QTimer()
            timer.singleShot(during * 1000, _delayedMsg)

    def _fcn_userRotation(self):
        """Display rotation informations.

        This function display rotation informations (azimuth / elevation /
        distance) at the bottom of the setting panel.
        """
        # Define and set the rotation string :
        rotstr = 'Azimuth: {az}°, Elevation: {el}°, Distance: {di}'
        # Get camera Azimuth / Elevation / Distance :
        az = str(self.view.wc.camera.azimuth)
        el = str(self.view.wc.camera.elevation)
        di = str(round(self.view.wc.camera.distance * 100) / 100)
        # Set the text to the box :
        self.userRotation.setText(rotstr.format(az=az, el=el, di=di))
