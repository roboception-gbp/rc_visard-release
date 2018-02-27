Name:           ros-indigo-rc-visard-driver
Version:        2.0.0
Release:        0%{?dist}
Summary:        ROS rc_visard_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://roboception.com/rc_visard
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       protobuf
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-rc-dynamics-api >= 0.5
Requires:       ros-indigo-rc-genicam-api
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-stereo-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-rc-dynamics-api >= 0.5
BuildRequires:  ros-indigo-rc-genicam-api
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-stereo-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs

%description
The rc_visard_driver provides data from a Roboception rc_visard 3D sensor on
several ROS topics.

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
* Tue Feb 27 2018 Felix Ruess <felix.ruess@roboception.de> - 2.0.0-0
- Autogenerated by Bloom

* Mon Feb 26 2018 Felix Ruess <felix.ruess@roboception.de> - 1.2.1-0
- Autogenerated by Bloom

* Sun Feb 11 2018 Heiko Hirschmueller <heiko.hirschmueller@roboception.de> - 1.2.0-0
- Autogenerated by Bloom

