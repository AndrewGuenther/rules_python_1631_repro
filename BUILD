load("@rules_python//python:defs.bzl", "py_binary")
load("@pip//:requirements.bzl", "requirement")

py_binary(
  name = "hello_world",
  srcs = ["hello_world.py", "my_module/__init__.py"],
  data = ["my_module/test.txt"],
  deps = [
    requirement("bazel-runfiles"),
  ]
)
