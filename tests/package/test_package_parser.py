from litemake.package import PackageInfo


def test_basic_package_info():
    info = PackageInfo(fieldpath=list(), data={
        'name': 'testing',
    })

    assert info.name == 'testing'
    assert info.version == (0, 0, 0)
    assert info.author is None
    assert info.description is None
    assert info.version_label is None
    assert info.identifier == 'testing-v0.0.0'


def test_package_custom_version():
    info = PackageInfo(fieldpath=list(), data={
        'name': 'testing',
        'version': {
            'major': 1,
            'minor': 2,
            'patch': 3,
            'label': 'dev',
        }
    })

    assert info.version == (1, 2, 3)
    assert info.version_label == 'dev'
    assert info.identifier == 'testing-v1.2.3-dev'
