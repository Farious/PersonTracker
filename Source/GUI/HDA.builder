<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <!-- interface-requires gtk+ 3.0 -->
  <object class="GtkWindow" id="MainFrame">
    <property name="can_focus">False</property>
    <property name="title" translatable="yes">PersonTracker</property>
    <property name="window_position">center-on-parent</property>
    <property name="type_hint">dialog</property>
    <child>
      <object class="GtkVBox" id="box1">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="orientation">vertical</property>
        <child>
          <object class="GtkMenuBar" id="menubar1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <child>
              <object class="GtkMenuItem" id="menuitem1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_File</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu1">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem1">
                        <property name="label">gtk-new</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem2">
                        <property name="label">gtk-open</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem3">
                        <property name="label">gtk-save</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem4">
                        <property name="label">gtk-save-as</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkSeparatorMenuItem" id="separatormenuitem1">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem5">
                        <property name="label">gtk-quit</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem2">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_Edit</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu2">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem6">
                        <property name="label">gtk-cut</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem7">
                        <property name="label">gtk-copy</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem8">
                        <property name="label">gtk-paste</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem9">
                        <property name="label">gtk-delete</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem3">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_View</property>
                <property name="use_underline">True</property>
              </object>
            </child>
            <child>
              <object class="GtkMenuItem" id="menuitem4">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">_Help</property>
                <property name="use_underline">True</property>
                <child type="submenu">
                  <object class="GtkMenu" id="menu3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <child>
                      <object class="GtkImageMenuItem" id="imagemenuitem10">
                        <property name="label">gtk-about</property>
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="use_underline">True</property>
                        <property name="use_stock">True</property>
                      </object>
                    </child>
                  </object>
                </child>
              </object>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="fill">True</property>
            <property name="position">0</property>
          </packing>
        </child>
        <child>
          <object class="GtkNotebook" id="notebook1">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="scrollable">True</property>
            <child>
              <object class="GtkHPaned" id="trackerPane">
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="position">546</property>
                <child>
                  <object class="GtkVBox" id="box3">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="orientation">vertical</property>
                    <child>
                      <object class="GtkDrawingArea" id="drawOpenGL">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                      </object>
                      <packing>
                        <property name="expand">True</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkHBox" id="buttonBox">
                        <property name="visible">True</property>
                        <property name="can_focus">False</property>
                        <property name="homogeneous">True</property>
                        <child>
                          <object class="GtkButton" id="goToBeginningBtn">
                            <property name="label">gtk-media-previous</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">0</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="previousFrameBtn">
                            <property name="label">gtk-media-rewind</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">1</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="stopBtn">
                            <property name="label">gtk-media-stop</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                            <property name="image_position">right</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">2</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="playBtn">
                            <property name="label">gtk-media-play</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">3</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="pauseBtn">
                            <property name="label">gtk-media-pause</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">4</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="nextFrameBtn">
                            <property name="label">gtk-media-forward</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">5</property>
                          </packing>
                        </child>
                        <child>
                          <object class="GtkButton" id="goToEndBtn">
                            <property name="label">gtk-media-next</property>
                            <property name="visible">True</property>
                            <property name="can_focus">True</property>
                            <property name="receives_default">True</property>
                            <property name="use_stock">True</property>
                          </object>
                          <packing>
                            <property name="expand">True</property>
                            <property name="fill">True</property>
                            <property name="position">6</property>
                          </packing>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="resize">False</property>
                    <property name="shrink">True</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkVBox" id="trackerExpanderBox">
                    <property name="visible">True</property>
                    <property name="can_focus">False</property>
                    <property name="orientation">vertical</property>
                    <child>
                      <object class="GtkExpander" id="personSelectorExp">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="label_fill">True</property>
                        <child>
                          <object class="GtkGrid" id="grid1">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="personSelectorExpLbl">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">Person Selector</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">0</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkExpander" id="videoSelectorExp">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="label_fill">True</property>
                        <child>
                          <object class="GtkGrid" id="grid2">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="videoSelectorExpLbl">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">Video Selector</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">1</property>
                      </packing>
                    </child>
                    <child>
                      <object class="GtkExpander" id="statistcsShowerExp">
                        <property name="visible">True</property>
                        <property name="can_focus">True</property>
                        <property name="label_fill">True</property>
                        <child>
                          <object class="GtkGrid" id="grid3">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                            <child>
                              <placeholder/>
                            </child>
                          </object>
                        </child>
                        <child type="label">
                          <object class="GtkLabel" id="statistcsShowerExpLbl">
                            <property name="visible">True</property>
                            <property name="can_focus">False</property>
                            <property name="label" translatable="yes">Statistics</property>
                          </object>
                        </child>
                      </object>
                      <packing>
                        <property name="expand">False</property>
                        <property name="fill">True</property>
                        <property name="position">2</property>
                      </packing>
                    </child>
                  </object>
                  <packing>
                    <property name="resize">False</property>
                    <property name="shrink">False</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="tab_expand">True</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="trackerPage">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">Tracker</property>
              </object>
              <packing>
                <property name="tab_fill">False</property>
              </packing>
            </child>
            <child>
              <object class="GtkFixed" id="fixed1">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
              </object>
              <packing>
                <property name="position">1</property>
                <property name="tab_expand">True</property>
              </packing>
            </child>
            <child type="tab">
              <object class="GtkLabel" id="rocPage">
                <property name="visible">True</property>
                <property name="can_focus">False</property>
                <property name="label" translatable="yes">ROC Curve</property>
              </object>
              <packing>
                <property name="position">1</property>
                <property name="tab_fill">False</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">True</property>
            <property name="fill">True</property>
            <property name="position">1</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
