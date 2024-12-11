%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-tuw-msgs
Version:        0.2.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tuw_msgs package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-tuw-airskin-msgs
Requires:       ros-jazzy-tuw-geometry-msgs
Requires:       ros-jazzy-tuw-graph-msgs
Requires:       ros-jazzy-tuw-multi-robot-msgs
Requires:       ros-jazzy-tuw-nav-msgs
Requires:       ros-jazzy-tuw-object-map-msgs
Requires:       ros-jazzy-tuw-object-msgs
Requires:       ros-jazzy-tuw-std-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-tuw-airskin-msgs
BuildRequires:  ros-jazzy-tuw-geometry-msgs
BuildRequires:  ros-jazzy-tuw-graph-msgs
BuildRequires:  ros-jazzy-tuw-multi-robot-msgs
BuildRequires:  ros-jazzy-tuw-nav-msgs
BuildRequires:  ros-jazzy-tuw-object-map-msgs
BuildRequires:  ros-jazzy-tuw-object-msgs
BuildRequires:  ros-jazzy-tuw-std-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-ament-lint-common
%endif

%description
tuw_msgs meta package with write and read file libs for tuw_msgs

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Dec 11 2024 Markus Bader <markus.bader@tuwien.ac.at> - 0.2.3-1
- Autogenerated by Bloom

* Thu Dec 05 2024 Markus Bader <markus.bader@tuwien.ac.at> - 0.2.2-1
- Autogenerated by Bloom

