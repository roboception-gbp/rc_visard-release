Name:           ros-indigo-rc-visard-description
Version:        2.4.2
Release:        0%{?dist}
Summary:        ROS rc_visard_description package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rc_visard_description
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Visualization package for rc_visard

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Oct 29 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.4.2-0
- Autogenerated by Bloom

* Wed Oct 24 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.4.0-0
- Autogenerated by Bloom

* Tue Aug 21 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.3.0-0
- Autogenerated by Bloom

* Tue Jul 03 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.2.0-0
- Autogenerated by Bloom

* Mon Apr 23 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.1.0-0
- Autogenerated by Bloom

* Tue Feb 27 2018 Monika Florek-Jasinska <monika.florek-jasinska@roboception.de> - 2.0.0-0
- Autogenerated by Bloom

