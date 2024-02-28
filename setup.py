from setuptools import find_packages, setup

package_name = 'fake_vel_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='md',
    maintainer_email='root@todo.todo',
    description='fake_vel_pub',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'vel_producer = fake_vel_pub.vel_producer:main',
		'vel_double = fake_vel_pub.vel_double:main',
        'vel_compare = fake_vel_pub.vel_compare:main',
        ],
    },
)
