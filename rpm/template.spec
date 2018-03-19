Name:           ros-melodic-unique-id
Version:        1.0.6
Release:        0%{?dist}
Summary:        ROS unique_id package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/unique_id
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-uuid-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-uuid-msgs

%description
ROS Python and C++ interfaces for universally unique identifiers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Mar 19 2018 Jack O'Quin <jack.oquin@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

