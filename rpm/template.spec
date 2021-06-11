%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rc-pick-client
Version:        3.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rc_pick_client package

License:        BSD
URL:            http://wiki.ros.org/rc_pick_client
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-rc-common-msgs
Requires:       ros-noetic-rcdiscover
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-shape-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-visualization-msgs
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-rc-common-msgs
BuildRequires:  ros-noetic-rcdiscover
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-shape-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The ros client for roboception grasp generation modules

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Jun 11 2021 Felix Ruess <felix.ruess@roboception.de> - 3.2.1-1
- Autogenerated by Bloom

* Tue Nov 24 2020 Felix Ruess <felix.ruess@roboception.de> - 3.1.0-1
- Autogenerated by Bloom

* Wed Oct 28 2020 Felix Ruess <felix.ruess@roboception.de> - 3.0.5-1
- Autogenerated by Bloom

* Wed Sep 23 2020 Felix Ruess <felix.ruess@roboception.de> - 3.0.4-1
- Autogenerated by Bloom

* Wed Aug 05 2020 Felix Ruess <felix.ruess@roboception.de> - 3.0.2-1
- Autogenerated by Bloom

