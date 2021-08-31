# nanomake

A new way to build, test and distribute your C/C++ projects and libraries.

## What is nanomake?

**nanomake** is a cross-platform CLI that aims to simplify the building, testing and distribution process of your C/C++ code.

By configuration a simple `setup.nanomake.toml` file, **nanomake** will be able to automatically:

- Download required dependencies and build you project
- Build only changed files to reduce compile time (similar to Make)
- Build and run your tests
- And more!

## The vision behind nanomake

There is a common phrase among the C/C++ developer community: *"(The convention) doesn't matter, just be consistent"* <sup>[1]</sup>. I however, strongly believe that a good convention is one that allows the developer to implement whatever he wants, but also allows others easily understand the intensions of the former. A good convention won't limit the developer, but will guide him.

### Compering to other programming languages

Other programming languages (mostly high-level ones like *Python* or *JavaScript*), have established package managers, build systems, and other tools to distribute your code, all all of that as a part of the programming language itself. Those tools allow developers to publish and download, build or install their package/library/project using a single command. Furthermore, developers can use other dependencies in their projects, and use other tools to improve their development including testing environments for example.

### And what about C/C++?

**nanomake** aims to bring the described above to the C/C++ community. By writing a simple configuration file `setup.nanomake.toml` and placing it in your project's root directory, users will be able to download all required dependencies, build and install your application just by using one command: `nanomake`.

Furthermore, with tools like [nanotest] you will be able to automatically build and run your tests. The sky is really the limit!

---

<div align="center">
    [learn more]
•   [documentation]
•   [nanotest]
•   [contribute]
</div>

<!-- Links -->

[toml]: https://toml.io/en/v1.0.0
[semver]: https://semver.org/
[nanotest]: link/to/nanotest

[1]: https://api.csswg.org/bikeshed/?force=1&url=https://raw.githubusercontent.com/vector-of-bool/pitchfork/develop/data/spec.bs#intro

