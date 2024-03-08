#!/usr/bin/env python3

import aws_cdk as cdk

from smart_gallery.smart_gallery_stack import SmartGalleryStack


app = cdk.App()
SmartGalleryStack(app, "SmartGalleryStack")

app.synth()
