# rc_visard

ROS interface for the [Roboception rc_visard][] 3D sensor.

## rc_visard_driver

Nodelet/node providing a ROS interface to configure the rc_visard and receive
images/poses. The minimum ROS version for the driver is Indigo.


### Build/Installation

This rc_visard_driver depends on

* [rc_genicam_api](https://github.com/roboception/rc_genicam_api)
* [rc_dynamics_api](https://github.com/roboception/rc_dynamics_api)

The dependencies can also be installed via rosdep.

    rosdep install --from-paths rc_visard_driver --ignore-src rc_visard_driver -r -y

Building and installing the package follows the typical ROS catkin workflow.

As an alternative, the cmake build-flow would be something like

    mkdir build && cd build
    cmake -DCATKIN_BUILD_BINARY_PACKAGE="1" -DCMAKE_INSTALL_PREFIX="/opt/ros/$ROS_DISTRO" -DCMAKE_PREFIX_PATH="/opt/ros/$ROS_DISTRO" -DCMAKE_BUILD_TYPE=Release ../rc_visard_driver
    make
    make install

Alternatively, instead of the final `make install`, you can also use
`make package` and `sudo dpkg -i install ros-indigo-rc-visard-driver_*.deb`.

### GenICam GenTL Transport Layer

The rc_visard_driver uses rc_genicam_api for interfacing with the rc_visard
sensor via GenICam/GigE Vision and requires a transport layer called a GenTL producer (shared library with the suffix `.cti`).
The path to this producer has to be set with the
`GENICAM_GENTL64_PATH` environment variable (or `GENICAM_GENTL32_PATH` for
32 bit systems).

For convenience rc_genicam_api comes with producers from Baumer for common
architectures.
If the `GENICAM_GENTL64_PATH` environment variable is not set, rc_visard_driver
will fall back to searching for the Baumer producer where rc_genicam_api is
installed.

If the producer .cti can't be found and you will get an error message like

    [ERROR] [1512568083.512790905]: rc_visard_driver: No transport layers found in path GENICAM_GENTL64_PATH

In this case you need either need to actually install rc_genicam_api properly or
set the environment variable when running it. E.g. export:

    GENICAM_GENTL64_PATH=/path/to/rc_genicam_api/baumer/Ubuntu-14.04/x86_64

### Configuration and usage

See the [rc_visard_driver README](rc_visard_driver/README.md) for more details.

## rc_visard_description

Package with xacro and urdf files for rc_visard_65 and rc_visard_160

### Build/Installation

Building and installing the package follows the typical ROS catkin workflow.

### Configuration and usage

See the [rc_visard_description README](rc_visard_description/README.md) for more details.


[Roboception rc_visard]: http://roboception.com/rc_visard
