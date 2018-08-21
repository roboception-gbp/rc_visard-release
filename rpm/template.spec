Name:           ros-indigo-rc-visard
Version:        2.3.0
Release:        0%{?dist}
Summary:        ROS rc_visard package

Group:          Development/Libraries
License:        BSD
URL:            http://roboception.com/rc_visard
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rc-visard-description
Requires:       ros-indigo-rc-visard-driver
BuildRequires:  ros-indigo-catkin

%description
Roboception rc_visard support meta package

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
* Tue Aug 21 2018 Felix Ruess <felix.ruess@roboception.de> - 2.3.0-0
- Autogenerated by Bloom

* Tue Jul 03 2018 Felix Ruess <felix.ruess@roboception.de> - 2.2.0-0
- Autogenerated by Bloom

* Mon Apr 23 2018 Felix Ruess <felix.ruess@roboception.de> - 2.1.0-0
- Autogenerated by Bloom

* Tue Feb 27 2018 Felix Ruess <felix.ruess@roboception.de> - 2.0.0-0
- Autogenerated by Bloom

* Mon Feb 26 2018 Heiko Hirschmueller <heiko.hirschmueller@roboception.de> - 1.2.1-0
- Autogenerated by Bloom

* Sun Feb 11 2018 Heiko Hirschmueller <heiko.hirschmueller@roboception.de> - 1.2.0-0
- Autogenerated by Bloom

