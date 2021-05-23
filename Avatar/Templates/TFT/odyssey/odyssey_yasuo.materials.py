#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Odyssey/Models/WoodenDoor_A/Materials/WoodenDoor_Paper_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/WoodenDoor_A/Materials/WoodenDoor_Paper_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/WoodenDoor_Paper_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/WoodenDoor_Paper_Mask_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MinValue"
                value: vec4 = { 0.150000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MaxValue"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flicker_Rate"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_AXIS_OFFSET_VALUE"
                value: vec4 = { 25, 0.25, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SPEED_RANDOMIZER_VALUE"
                value: vec4 = { 1, 0.200000003, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_VERTEX_ANIMATION"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Lantern"
                        cullEnable: bool = false
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Odyssey_Tree_C/Materials/Odyssey_Tree_C_VertexColor_Multiply_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Odyssey_Tree_C/Materials/Odyssey_Tree_C_VertexColor_Multiply_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_TreeCanopy_Yasuo.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Env_Diffuse_VertexColor_Multiply"
                        blendEnable: bool = true
                        cullEnable: bool = false
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Board_B/Materials/Board_B_Pulse_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Board_B/Materials/Board_B_Pulse_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Board_B.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Board_B_Mask.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Range"
                value: vec4 = { 0.589999974, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Pulse_Rate"
                value: vec4 = { 1.27499998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Center"
                value: vec4 = { 0.5, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_RotationSpeed"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_Tiling"
                value: vec4 = { 13, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_Offset"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MaskSpotlight_Offset"
                value: vec4 = { -6.5, -6, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_Dims"
                value: vec4 = { 3, 3, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_FPS"
                value: vec4 = { 9, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScanLine_rate"
            }
            StaticMaterialShaderParamDef {
                name: string = "ScanLine_amount"
                value: vec4 = { 927.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScanLine_minmax"
                value: vec4 = { -4, 4, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_OVERLAY"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ANIMATEDMASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_FLIPBOOK_ROTATION"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_FLIPBOOK_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_SCANLINES"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_DIffuse_Pulse"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Glass_Bottle_A/Materials/ENV_Glass_Malphite_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Glass_Bottle_A/Materials/ENV_Glass_Malphite_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Glass_Roughness"
                value: vec4 = { 0.200000003, 0.0784313753, 0.0784313753, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size_Inner"
                value: vec4 = { 60.3205757, 0.286274523, 0.411764711, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SunColor"
                value: vec4 = { 0.910002291, 0.86999315, 0.530006886, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glass_Color2"
                value: vec4 = { 0.650003791, 0.650003791, 0.650003791, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glass_Color1"
                value: vec4 = { 0.149996191, 0.149996191, 0.149996191, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size_Outer"
                value: vec4 = { 1.76972508, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Bias"
                value: vec4 = { -0.234999999, 0.0313725509, 0.286274523, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Glass"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Odyssey_Tree_A/Materials/Odyssey_Tree_VertexColor_Multiply_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Odyssey_Tree_A/Materials/Odyssey_Tree_VertexColor_Multiply_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_TreeCanopy_Yasuo.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Env_Diffuse_VertexColor_Multiply"
                        blendEnable: bool = true
                        cullEnable: bool = false
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/PaperLantern_A/Materials/ENV_Lantern_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/PaperLantern_A/Materials/ENV_Lantern_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/PaperLantern_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/PaperLantern_Mask_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size"
                value: vec4 = { 3.52945018, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MinValue"
                value: vec4 = { 0.502499998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MaxValue"
                value: vec4 = { 0.805000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flicker_Rate"
                value: vec4 = { 0.875, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_AXIS_OFFSET_VALUE"
                value: vec4 = { 10, -2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SPEED_RANDOMIZER_VALUE"
                value: vec4 = { 2.5, 0.5, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_VERTEX_ANIMATION"
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Lantern"
                        cullEnable: bool = false
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Monitor_Large_A/Materials/ENV_MonitorScreen_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Monitor_Large_A/Materials/ENV_MonitorScreen_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/MonitorScreen_A.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "UV_TileAmount"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Bottom"
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Softness"
                value: vec4 = { 100, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Offset"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_OBJECT_GRADIENT"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_TileableDiffuse"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Yasuo_Creature_A/Materials/ENV_YasuoCreature_Vertex_Expand_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Yasuo_Creature_A/Materials/ENV_YasuoCreature_Vertex_Expand_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Yasuo_Creature_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Frequency"
                value: vec4 = { 1.20000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Magnitude"
                value: vec4 = { 8, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Lower_Limit"
                value: vec4 = { -0.0199999996, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Upper_Limit"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Diffuse_Vertex_Expand"
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Trunk" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Trunk"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_TreeTrunk.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Canopy" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Canopy"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_TreeCanopy.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Perch_Yasuo_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Perch_Yasuo_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Perch_Yasuo_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Candles_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Candles_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Candles_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Wood_Floor_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Wood_Floor_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Wood_Floor_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Misc_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Misc_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Misc_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Pipes_Modular_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Pipes_Modular_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Pipes_Modular_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Misc_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Misc_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Misc_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Engine_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Engine_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Engine_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Metal_Tileable_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Metal_Tileable_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Metal_Panels_Tileable_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_Malphite_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_Malphite_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_Malphite_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Zengarden_Yasuo_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Zengarden_Yasuo_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Zengarden_Yasuo_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/YasuoSword_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/YasuoSword_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/YasuoSword_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Rug_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Rug_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Rug_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_Yasuo_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_Yasuo_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_Yasuo_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_Yasuo_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_Yasuo_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Stripes_Yasuo_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Metal_Tileable_A1" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Metal_Tileable_A1"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Metal_Panels_Tileable_A.TFT_ArenaSkin_Galaxy2.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Yasuo_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Yasuo_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Yasuo.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_Yasuo_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_Yasuo_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Bench_Yasuo_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Canopy_Yasuo" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Odyssey_Tree_Canopy_Yasuo"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_TreeCanopy_Yasuo.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/TreePlanter_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/TreePlanter_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/TreePlanter_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Ship_Hull_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Ship_Hull_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Ship_Hull_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Books_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Books_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Books_A.TFT_ArenaSkin_Odyssey.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Project/Models/Buildings/prj_building_01/Materials/dark_blue_Emissive_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Project/Models/Buildings/prj_building_01/Materials/dark_blue_Emissive_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { 0.168627456, 0.31764707, 0.513725519, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 0.75, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0.699999988, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Emissive_Basic"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Project/Models/Buildings/prj_building_01/Materials/light_blue_Emissive_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Project/Models/Buildings/prj_building_01/Materials/light_blue_Emissive_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { 0.250980407, 0.549019635, 0.596078455, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 0.699999988, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0.550000012, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Emissive_Basic"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_DustShadows" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            20
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "glowLight1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 30 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 2
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.505882382, 1, 0.917647064, 0.298039228 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.505882382, 1, 0.917647064, 0 }
                            { 0.505882382, 1, 0.917647064, 0.298039228 }
                            { 0.505882382, 1, 0.917647064, 0 }
                        }
                    }
                }
                pass: i16 = 2000
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 180, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 2000, 50 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 0.300000012, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Light.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Hangar_DustShadows"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_DustShadows"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Station_Amb" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Station_Amb"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Station_Amb"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_station_amb"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "ship"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.00100000005, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_JetA.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "thinTrial"
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 10000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 2000, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.510002315, 0.889997721, 1, 1 }
                            { 0.469993144, 0.800000012, 1, 1 }
                            { 0.329411775, 0.529411793, 1, 1 }
                            { 0.266666681, 0.31764707, 0.992156863, 0.294117659 }
                            { 0.203921571, 0.203921571, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 100, 0 }
                }
                texture: string = "ASSETS/Perks/Styles/Sorcery/ArcaneComet/Particles/Perks_Meteor_Simple_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1.5, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "BigSoft"
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 10000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 2000, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.510002315, 0.889997721, 1, 1 }
                            { 0.469993144, 0.800000012, 1, 1 }
                            { 0.329411775, 0.529411793, 1, 1 }
                            { 0.266666681, 0.31764707, 0.992156863, 0.294117659 }
                            { 0.203921571, 0.203921571, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 100, 0 }
                }
                texture: string = "ASSETS/Perks/Styles/Sorcery/ArcaneComet/Particles/Perks_Meteor_Simple_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1.5, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "ship1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.00100000005, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.188235298, 0.403921574, 1, 1 }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_JetA_jets.TFT_ArenaSkin_Odyssey.dds"
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_Ship_Child"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship_Child"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_common_jet_distant"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Volume" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.800000012, 0.489997715, 0.100007631 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.800000012, 0.489997715, 0 }
                            { 1, 0.800000012, 0.489997715, 0.100007631 }
                            { 1, 0.800000012, 0.489997715, 0 }
                        }
                    }
                }
                pass: i16 = -50
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1100, 800, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Yasuo_RoundGlow.TFT_ArenaSkin_Odyssey.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Hangar_Volume"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Volume"
        buildUpTime: f32 = 4
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_B_Drones" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 500
        particleName: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_B_Drones"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_B_Drones"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_lanterns_b_drones"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireDown_glow_blend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.36470589, 1, 0.960784316, 0 }
                            { 0.447058827, 1, 0.882352948, 1 }
                            { 0.333333343, 0.709803939, 0.509803951, 0 }
                        }
                    }
                }
                pass: i16 = -3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Trail_Mult.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0.0117647061, 0.75686276, 0.0980392173, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_20.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.5 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireUp_glow_Blend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Upper_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.545098066, 0.956862748, 1, 0 }
                            { 0.278431386, 1, 0.894117653, 1 }
                            { 0.129411772, 0.709803939, 0.564705908, 0 }
                        }
                    }
                }
                pass: i16 = -2
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Base_UnderGlow.TFT_Set3.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.5 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "wireDown_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Trait_Elementalist_Smoke_Mult.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireUp_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Upper_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 0.990005314, 0.100007631 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/alphaslice_mesh.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.588235319, 0.494117647, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.25 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                isSingleParticle: flag = true
                emitterName: string = "wire_turnon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.0431372561, 0.498039216, 0.709803939, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "wireDown_glow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Trait_Elementalist_Smoke_Mult.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "jjFlare"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -1, 22, 6 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.345098048, 0.913725495, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.345098048, 0.913725495, 1, 0 }
                            { 0.345098048, 0.913725495, 1, 0.800000012 }
                            { 0.345098048, 0.913725495, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 100, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 100, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Slash_Flare.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "jjFlare1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -1, 22, 6 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.345098048, 0.913725495, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.345098048, 0.913725495, 1, 0 }
                            { 0.345098048, 0.913725495, 1, 0.800000012 }
                            { 0.345098048, 0.913725495, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Base_Sparks.dds"
            }
        }
        particleName: string = "TFT_GoldMine_Odyssey_Yasuo_Start"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Door_Dust" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            20
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_DustShadows"
                        }
                    }
                }
                emitterName: string = "Motes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0199999996, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.0199999996, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -5, -2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -5, -2 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1, -1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1, -1 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 300, 300 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 300, 300 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 500
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1.79999995, 1.79999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 1.79999995, 1.79999995 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.699999988, 0.699999988, 0.699999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/HA_PoroRay_snow_glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Door_Dust"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Door_Dust"
        buildUpTime: f32 = 5
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Smoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            30
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "smokyMist"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 2.5, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2.5, 1, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 5, 350 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 5, 350 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -1
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    0
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.170000762 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.170000762 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.678431392, 0.352941185, 0 }
                            { 0.937254906, 0.68235296, 0.458823532, 1 }
                            { 0.305882365, 0.41568628, 0.509803951, 1 }
                            { 0.137254909, 0.262745112, 0.411764711, 0 }
                        }
                    }
                }
                pass: i16 = -10
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -8 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -20, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Shared/Particles/Morde_Base_Dust.TFT_Set4_Act2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            30
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "smokyMistAlpha"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 2.5, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2.5, 1, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 5, 350 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 5, 350 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -1
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    0
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149996191 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.149996191 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.745098054, 0.490196079, 0 }
                            { 0.937254906, 0.752941191, 0.568627477, 1 }
                            { 0.509803951, 0.627451003, 0.717647076, 1 }
                            { 0.31764707, 0.494117647, 0.678431392, 0 }
                        }
                    }
                }
                pass: i16 = -11
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -8 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -20, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Shared/Particles/TFT_Illaoi_Dust.TFT_Set3.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_Hangar_Smoke"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Smoke"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_steam"
        buildUpTime: f32 = 10
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 500, 0 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 20
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 100
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "Gold"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 250, 1500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1, 3 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 72, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 175, 0, 135 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectRadius: f32 = 0.00499999989
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.788235307, 1, 0.627451003, 1 }
                            { 0, 1, 0.466666669, 1 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { 1, 1 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Qbv2_Gold.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0.590005338, 0.319996953, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 9, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "orb"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 120, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Janna_Skin08_Wind_Swipe.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.729411781 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.729411781 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.305882365, 0.694117665, 0.337254912, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.305882365, 0.694117665, 0.337254912, 0 }
                            { 0.305882365, 0.694117665, 0.337254912, 1 }
                            { 0.305882365, 0.694117665, 0.337254912, 0 }
                        }
                    }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Shared/Particles/alphaslice_mesh.ARAM_VFX_Update.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3.79999995, 10, 3.79999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3.79999995, 10, 3.79999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_WispTrail_Add.ARAM_VFX_Update.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 1, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 4, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.35000002
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.294117659, 1, 0.243137255, 0.360784322 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 120
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 150, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 1, 1 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "blueFire"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -1
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    45
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.160784319, 0.850980401, 0.474509805, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.160784319, 0.850980401, 0.474509805, 0 }
                            { 0.160784319, 0.850980401, 0.474509805, 1 }
                            { 0.039723184, 0.614040732, 0.323783159, 1 }
                            { 0.00126105349, 0, 0.266097665, 0 }
                        }
                    }
                }
                pass: i16 = 51
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 150
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 450, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "orb1"
                disabled: bool = true
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 120, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Janna_Skin08_Wind_Swipe.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.729411781 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.729411781 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.741176486, 0.427450985, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.0666666701, 0.741176486, 0.427450985, 0 }
                            { 0.0666666701, 0.741176486, 0.427450985, 1 }
                            { 0.0666666701, 0.741176486, 0.427450985, 0 }
                        }
                    }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Shared/Particles/alphaslice_mesh.ARAM_VFX_Update.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3.79999995, 10, 3.79999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3.79999995, 10, 3.79999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_WispTrail_Add.ARAM_VFX_Update.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 1, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 9, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "longGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 200, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.274509817, 1, 0.733333349, 0.741176486 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.274509817, 1, 0.733333349, 0 }
                            { 0.274509817, 1, 0.733333349, 0.741176486 }
                            { 0.274509817, 1, 0.733333349, 0 }
                        }
                    }
                }
                pass: i16 = 500
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 1000, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_JetThruster_01"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_01"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.25
                        }
                    }
                }
                emitterName: string = "Gold"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 350, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 72, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 250, 0, 135 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectRadius: f32 = 0.00499999989
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec4] = {
                            { 0.788235307, 1, 0.627451003, 1 }
                            { 0, 1, 0.466666669, 1 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { 1, 1 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Qbv2_Gold.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0.590005338, 0.319996953, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "orb"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 120, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Janna_Skin08_Wind_Swipe.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.729411781 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.729411781 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.305882365, 0.694117665, 0.337254912, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.305882365, 0.694117665, 0.337254912, 0 }
                            { 0.305882365, 0.694117665, 0.337254912, 1 }
                            { 0.305882365, 0.694117665, 0.337254912, 0 }
                        }
                    }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Shared/Particles/alphaslice_mesh.ARAM_VFX_Update.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4.5, 10, 4.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 4.5, 10, 4.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_WispTrail_Add.ARAM_VFX_Update.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 1, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.35000002
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.294117659, 1, 0.243137255, 0.360784322 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 120
                }
                depthBiasFactors: vec2 = { -1, -2 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 750, 150, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 1, 1 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "blueFire"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 150, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -1
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    45
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.160784319, 0.839215696, 0.466666669, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.160784319, 0.839215696, 0.466666669, 0 }
                            { 0.160784319, 0.839215696, 0.466666669, 1 }
                            { 0.039723184, 0.60555172, 0.318431377, 1 }
                            { 0.00126105349, 0, 0.261699349, 0 }
                        }
                    }
                }
                pass: i16 = 51
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 150
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -1 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "longGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 200, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.274509817, 1, 0.733333349, 0.741176486 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.274509817, 1, 0.733333349, 0 }
                            { 0.274509817, 1, 0.733333349, 0.741176486 }
                            { 0.274509817, 1, 0.733333349, 0 }
                        }
                    }
                }
                pass: i16 = 500
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 1000, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_JetThruster_02"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_02"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar_Child"
                        }
                    }
                }
                emitterName: string = "cometParentFast"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.150000006, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 4000, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 1, 0, 0 }
                    }
                }
                blendMode: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/disc32.TFT_Set4.DDS"
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_ShootingStar"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Amb2D" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Amb2D"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Amb2D"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_amb2d"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 0, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.790005326, 0.149996191, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.790005326, 0.149996191, 0 }
                            { 1, 0.790005326, 0.149996191, 0.400000006 }
                            { 1, 0.790005326, 0.149996191, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 20
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_UnitCombination_Bigglow02.SKINS_Veigar_Skin23.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/alphaslice_mesh.TFT_Set5.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "glowLight"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.669993162, 0.149996191, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.669993162, 0.149996191, 0 }
                            { 1, 0.669993162, 0.149996191, 0.500007629 }
                            { 1, 0.669993162, 0.149996191, 0 }
                        }
                    }
                }
                pass: i16 = 500
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Odyssey_Yasuo_ShipLightFog"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start_Away" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireDown_glow_blend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.36470589, 1, 0.960784316, 0 }
                            { 0.447058827, 1, 0.882352948, 1 }
                            { 0.333333343, 0.709803939, 0.509803951, 0 }
                        }
                    }
                }
                pass: i16 = -3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Trail_Mult.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0.0117647061, 0.75686276, 0.0980392173, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_20.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.5 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireUp_glow_Blend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Upper_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.545098066, 0.956862748, 1, 0 }
                            { 0.278431386, 1, 0.894117653, 1 }
                            { 0.129411772, 0.709803939, 0.564705908, 0 }
                        }
                    }
                }
                pass: i16 = -2
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Base_UnderGlow.TFT_Set3.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.5 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "wireDown_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Trait_Elementalist_Smoke_Mult.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "wireUp_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Upper_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 0.990005314, 0.100007631 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/alphaslice_mesh.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.588235319, 0.494117647, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.25 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                isSingleParticle: flag = true
                emitterName: string = "wire_turnon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.0431372561, 0.498039216, 0.709803939, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "wireDown_glow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Goldmine_Lower_Start.TFT_ArenaSkins_Odyssey_Frontend.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.909803927, 1, 0.631372571 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.709803939, 0.388235301, 0.129411772, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                0.100000001
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Trait_Elementalist_Smoke_Mult.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "jjFlare"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -1, 22, -2 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.345098048, 0.913725495, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.345098048, 0.913725495, 1, 0 }
                            { 0.345098048, 0.913725495, 1, 0.800000012 }
                            { 0.345098048, 0.913725495, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 100, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 100, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Slash_Flare.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "jjFlare1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -1, 22, -2 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.345098048, 0.913725495, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.345098048, 0.913725495, 1, 0 }
                            { 0.345098048, 0.913725495, 1, 0.800000012 }
                            { 0.345098048, 0.913725495, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Base_Sparks.dds"
            }
        }
        particleName: string = "TFT_GoldMine_Odyssey_Yasuo_Start_Away"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start_Away"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0350000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowbright"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_B_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowConstant"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_B_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Tree_B_Shimmer"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Skybox_Odyssey_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -140, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_BGClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Stars01.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 0.800000012 }
                }
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "BlueClouds"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 190, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_MGClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.349996179, 0.689997733, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.400000006, 0.590005338, 1, 0.310002297 }
                }
                pass: i16 = 6
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.0399999991, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PurpleCloud01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 2 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "BlueClouds1"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 190, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_MGClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.719996929, 0.960006118, 1, 0.710002303 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.469993144, 0.900007606, 1, 0.639993906 }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PurpleCloud01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "CloudNoiseA"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 170, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_CloudNoise.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.862745106, 0.886274517, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            10
                            30
                        }
                        values: list[vec4] = {
                            { 0.379602581, 0.886274517, 0.97999543, 0.489997715 }
                            { 0.422743112, 0.691290081, 1, 0.919996977 }
                            { 0.500388205, 0.886274517, 0.970000744, 0.379995435 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.850980401, 0.898039222, 0.960784316, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            10
                            30
                        }
                        values: list[vec4] = {
                            { 0.502083004, 0.862123132, 0.960784316, 0.0200045779 }
                            { 0.536117017, 0.898039222, 0.893536031, 0.900007606 }
                            { 0.476554215, 0.691490889, 0.960784316, 0.439993888 }
                        }
                    }
                }
                pass: i16 = 18
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_CloudyNoise02.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00499999989, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "FloatingRock3"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 30, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_RockLayerC.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.719996929, 0.829999208, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.76000613, 0.910002291, 1, 1 }
                }
                pass: i16 = 13
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00200000009, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "FloatingRock1"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 70, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_RockLayer.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.847058833, 0.862745106, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.933333337, 0.956862748, 1, 1 }
                }
                pass: i16 = 17
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.180000007, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "FloatingRock2"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 80, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_RockLayerB.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.917647064, 0.921568632, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.921568632, 0.956862748, 1, 1 }
                }
                pass: i16 = 15
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00499999989, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Light"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 140, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_BOTClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.300007641, 0.579995394, 0.710002303, 0.549996197 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.310002297, 0.749996185, 0.779995441, 0.469993144 }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Lightbelt.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Light1"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 160, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_BOTClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.352941185, 0.662745118, 0.839215696, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.572549045, 0.996078432, 1, 0.933333337 }
                }
                pass: i16 = 11
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Lightbelt.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Star_Detail"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -120, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_BGClouds.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.850003839 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.620004594 }
                }
                pass: i16 = 3
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_StarsC.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00499999989, 0 }
                }
                texDiv: vec2 = { 2, 2 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "CloudNoiseA1"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 170, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_CloudNoise.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.698039234, 0.847058833, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            10
                            30
                        }
                        values: list[vec4] = {
                            { 0.307132989, 0.847058833, 0.97999543, 0.0399938971 }
                            { 0.342037618, 0.66070199, 1, 0.949996173 }
                            { 0.404859543, 0.847058833, 0.970000744, 0.379995435 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.694117665, 0.815686285, 0.960784316, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            10
                            30
                        }
                        values: list[vec4] = {
                            { 0.409533113, 0.783063829, 0.960784316, 0.0399938971 }
                            { 0.437293589, 0.815686285, 0.893536031, 0.990005314 }
                            { 0.388710111, 0.628079057, 0.960784316, 0.420004576 }
                        }
                    }
                }
                pass: i16 = 19
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_CloudyNoise03.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "PlanetA"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 70, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_PlanetA.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 4
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PlanetB.dds"
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_Odyssey_B"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Skybox_Odyssey_B"
        flags: u8 = 197
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Space_Mist" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 35
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            35
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "brightMist"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, -1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, -1 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 20 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2500, 5, 2500 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 2500, 5, 2500 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.556862772, 1, 0.698039234, 0.298039228 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.246766627, 1, 0.131395623, 0 }
                            { 0.0742483661, 1, 0.375025004, 0.298039228 }
                            { 0.0327566303, 0.56078434, 0.698039234, 0.298039228 }
                            { 0.115740098, 0.258823544, 0.698039234, 0 }
                        }
                    }
                }
                pass: i16 = 17
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 500
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -8 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2000, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2000, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Shared/Particles/Morde_Base_Dust.TFT_Set4_Act2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            20
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "darkMist"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, -1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, -1 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 20 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2500, 5, 2500 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 2500, 5, 2500 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.694117665, 1, 0.647058845, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.694117665, 1, 0.647058845, 0 }
                            { 0.694117665, 1, 0.647058845, 1 }
                            { 0.168765858, 1, 0.606459081, 1 }
                            { 0.182376012, 0.768627465, 0.647058845, 0 }
                        }
                    }
                }
                pass: i16 = 16
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 500
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -8 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1800, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1800, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Shared/Particles/Morde_Base_Dust.TFT_Set4_Act2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 35
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            35
                        }
                    }
                }
                emitterName: string = "brightMotes"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, -2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, -2 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.949999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 20 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2500, 1000, 2500 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 2500, 1000, 2500 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.870588243, 0.396078438, 0 }
                            { 0.760784328, 1, 0.203921571, 0.500007629 }
                            { 0.160784319, 1, 0.972549021, 0.22549364 }
                            { 0, 0.650980413, 1, 0 }
                        }
                    }
                }
                pass: i16 = 16
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0465116277
                            0.0852713212
                            0.120930232
                            0.158139542
                            0.172093019
                            0.212403104
                            0.248062015
                            0.285271317
                            0.316279083
                            0.38139534
                            0.4108527
                            0.446511626
                            0.472868204
                            0.506976724
                            0.604651153
                            0.638759673
                            0.674418628
                            0.736434102
                            0.772092998
                            0.815503895
                            0.858914733
                            0.933333337
                            0.973643422
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.079136692, 0.985724688, 0.985724688 }
                            { 0.719424486, 0.972591341, 0.972591341 }
                            { 0.0863309354, 0.958887041, 0.958887041 }
                            { 0.949640274, 0.945182741, 0.945182741 }
                            { 0.323741019, 0.905592442, 0.905592442 }
                            { 0.705035985, 0.870570302, 0.870570302 }
                            { 0.25179857, 0.834025502, 0.834025502 }
                            { 1, 0.803571463, 0.803571463 }
                            { 0.100719422, 0.739617944, 0.739617944 }
                            { 0.978417277, 0.710686624, 0.710686624 }
                            { 0.223021582, 0.675664485, 0.675664485 }
                            { 0.848920882, 0.649778545, 0.649778545 }
                            { 0.258992791, 0.616279066, 0.616279066 }
                            { 1, 0.494186044, 0.494186044 }
                            { 0.223021582, 0.451550394, 0.451550394 }
                            { 0.935251772, 0.40697673, 0.40697673 }
                            { 0.16546762, 0.329457372, 0.329457372 }
                            { 0.820143878, 0.284883708, 0.284883708 }
                            { 0.115107916, 0.230620146, 0.230620146 }
                            { 0.791366935, 0.176356584, 0.176356584 }
                            { 0.079136692, 0.0833333284, 0.0833333284 }
                            { 0.517985582, 0.0329457335, 0.0329457335 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ziggs_Skin05_EnergyMote.dds"
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_Space_Mist"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Space_Mist"
        flags: u8 = 212
        buildUpTime: f32 = 5
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_A_Shimmer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0560000017
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowBright"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_A_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowConstant"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_A_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Tree_A_Shimmer"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_A_Shimmer"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            12
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 1 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 500, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 500, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.627451003, 0.376470596, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 0.627451003, 0.376470596, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    3
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 1, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.100000001
                                    0.100000001
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Particles/ChoDino_Dust.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.400000006
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Wind1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 400, 0, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 500, 0, 500 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 500, 0, 500 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.729411781, 0.41568628, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 0.729411781, 0.41568628, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 140, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10.5, 4.5, 7.5 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0 }
                }
                texAddressModeBase: u8 = 2
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "TFT_Odyssey_Yasuo_Wind"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Wind"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_A_Drones" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 500
        particleName: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_A_Drones"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_A_Drones"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_lanterns_a_drones"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "END_Beam_ROTATING"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/color-hold.TFT_Set5.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.564705908, 0.0666666701, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 221
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 180, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 180, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.159999996, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.0799999982, 0.0799999982, 0.0799999982 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Diana_Skin11_E_Glow.TFT_ArenaSkin_Odyssey.dds"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Core4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.749996185, 0, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.647059023, 0.0117650004, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 2
                colorLookUpTypeX: u8 = 3
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 30, 20 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_flash_cas.TFT_ArenaSkin_Odyssey.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Core_White"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.701960802, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.701960802, 1, 0 }
                            { 0, 0.701960802, 1, 1 }
                            { 0, 0.00825856905, 0.0117650004, 0 }
                        }
                    }
                }
                pass: i16 = 2
                colorLookUpTypeX: u8 = 3
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 30, 20 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_flash_cas.TFT_ArenaSkin_Odyssey.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Core_White1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.0800030529 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 0.450980395, 0.647058845, 0 }
                        }
                    }
                }
                pass: i16 = 15
                colorLookUpTypeX: u8 = 3
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 30, 20 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_BA_Prism.TFT_ArenaSkin_Odyssey.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            150
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.150000006
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Sparks_1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.100000001, 0.100000001, 0.100000001 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 55, -10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -0, 165, -0 }
                            { -10, 27.5, -10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 2, 2 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -20
                                        20
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -25
                                        25
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 2, 2, 2 }
                            }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.650980413, 1, 1 }
                            { 0.149019614, 1, 0.576470613, 1 }
                            { 0.00784313772, 0.145098045, 0.443137258, 0 }
                        }
                    }
                }
                colorLookUpTypeX: u8 = 3
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 12, 12 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.649999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6, 12, 12 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                            { 0.100000001, 0.100000001, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Emote_Mote.TFT_ArenaSkin_Odyssey.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 9, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "distort_BB"
                importance: u8 = 0
                keywordsExcluded: list[string] = {
                    "SteelLegionLux"
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                pass: i16 = 1
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 0.5, 1 }
                colorLookUpOffsets: vec2 = { 0.5, 0 }
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0500000007
                    distortionMode: u8 = 3
                    normalMapTexture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_BA_Distort_Blurred.TFT_ArenaSkin_Odyssey.dds"
                }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 325, 325 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Aura_Self.TFT_Set5.dds"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 325
                }
                particleBind: vec2 = { 1, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "nega_fixed_ADD"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, 10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Emote_FlickeringMask_1.TFT_ArenaSkin_Odyssey.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.360784322, 0.800000012, 1, 1 }
                }
                pass: i16 = 999
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -15 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 6 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1.5, 1.5 }
                            { 0.699999988, 0.5, 0.5 }
                            { 1, 1.5, 1.5 }
                            { 0.600000024, 0.200000003, 0.200000003 }
                            { 1, 1.5, 1.5 }
                            { 0.699999988, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_BA_energycircle03.TFT_ArenaSkin_Odyssey.dds"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[f32] = {
                            0
                            1
                            0
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                birthRotationalVelocity1: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            200
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                emitterName: string = "END_Beam_ROTATING1"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/color-hold.TFT_Set5.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.349019617, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 221
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 120, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 8, 120, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.159999996, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.0799999982, 0.0799999982, 0.0799999982 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Diana_Skin11_E_Glow.TFT_ArenaSkin_Odyssey.dds"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    3
                }
                emitterName: string = "LongTrail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 550, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 550, 5 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 8, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 5, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 65, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 65, 10, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.360006094, 0.800000012, 1, 0.839993894 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.466666669, 0, 1, 1 }
                        }
                    }
                }
                pass: i16 = 222
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 20, 6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 20, 6 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.20000005, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.649999976
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1.79999995, 1.5 }
                            { 0.5, 0.600000024, 0.5 }
                            { 1, 1.79999995, 1.5 }
                            { 0.75, 1.79999995, 1.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Q_Small_Mote.TFT_ArenaSkin_Odyssey.dds"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[f32] = {
                            0
                            1
                            0
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                birthRotationalVelocity1: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            200
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Pillar_bk2"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 10, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/color-hold.TFT_Set5.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.480003059, 0.600000024, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.255798548
                            0.572895944
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.521568656, 0.913725495, 1, 1 }
                            { 0.0980392173, 1, 0.925490201, 0.521568656 }
                            { 0, 0.400000006, 1, 0.0980392173 }
                            { 0.498039216, 0.0588235296, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0.0500000007
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_R_ErosionPack01.TFT_ArenaSkin_Odyssey.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 200, 10 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 1.20000005, 0 }
                            { 1, 0.75, 1 }
                            { 1, 0.150000006, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_SmokeTip.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Q_RainbowMult02.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Pillar_bk3"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 10, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 10, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/color-hold.TFT_Set5.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.480003059, 0.600000024, 1, 0.450003803 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.480003059, 0.600000024, 1, 0.450003803 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.521568656, 0.913725495, 1, 1 }
                            { 0.100007631, 1, 0.930006862, 1 }
                            { 0, 0.400000006, 1, 0.0980392173 }
                            { 0.498039216, 0.0588235296, 1, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.349999994
                                1
                            }
                            values: list[f32] = {
                                0
                                0.0399999991
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_R_ErosionPack01.TFT_ArenaSkin_Odyssey.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 200, 10 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 1.20000005, 0 }
                            { 1, 0.75, 1 }
                            { 1, 0.150000006, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_SmokeTip.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Q_RainbowMult02.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "cone_add"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 105, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            1
                            0.800000012
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Sharp_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/color-hold.TFT_Set5.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.130006865, 0.519996941, 1, 0.7400015 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.130006865, 0.519996941, 1, 0 }
                            { 0.130006865, 0.519996941, 1, 0.7400015 }
                            { 0.130006865, 0.519996941, 1, 0.7400015 }
                            { 0.130006865, 0.519996941, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.549019635, 0.768627465, 1, 1 }
                            { 0.454901963, 0, 0.97647059, 1 }
                            { 1, 0, 0.431372553, 0 }
                        }
                    }
                }
                pass: i16 = 5
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 20
                    deltaIn: f32 = 10
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/alphaslice_mesh.TFT_Set5.dds"
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, -90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 180, -90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 1.20000005, 0.600000024, 0.600000024 }
                            { 2, 1, 1 }
                            { 2.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_BlastRing.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Mult_Windblast.TFT_ArenaSkin_Odyssey.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "nega_fallthrough"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, 10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 5, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 40, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Emote_FlickeringMask_1.TFT_ArenaSkin_Odyssey.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.360784322, 0.800000012, 1, 1 }
                }
                pass: i16 = 999
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -15 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 20, 6 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1.5, 1.5 }
                            { 0.699999988, 0.5, 0.5 }
                            { 0.800000012, 1.5, 1.5 }
                            { 0.349999994, 0.200000003, 0.200000003 }
                            { 0.5, 1.5, 1.5 }
                            { 0, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_BA_energycircle03.TFT_ArenaSkin_Odyssey.dds"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[f32] = {
                            0
                            1
                            0
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                birthRotationalVelocity1: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            200
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "nega_fixed_ADD1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, 10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 45, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 45, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/Lux_Skin18_Q_FlickeringMask_1.TFT_ArenaSkin_Odyssey.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.149019614, 0.960784316, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 999
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -15 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 20, 6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 20, 6 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1.5, 1.5 }
                            { 0.699999988, 0.5, 0.5 }
                            { 1, 1.5, 1.5 }
                            { 0.600000024, 0.200000003, 0.200000003 }
                            { 1, 1.5, 1.5 }
                            { 0.699999988, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Diana_Skin11_Q_Glow.TFT_ArenaSkin_Odyssey.dds"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                scale1: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[f32] = {
                            0
                            1
                            0
                        }
                    }
                }
                birthRotation1: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                birthRotationalVelocity1: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            200
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "dustyTrail"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 40, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 10000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 3000, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.639215708, 0.627451003, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.325874656, 0.56101501, 1, 0 }
                            { 0.30042699, 0.501960814, 1, 1 }
                            { 0.210565165, 0.332179934, 1, 1 }
                            { 0.170457512, 0.199307963, 0.992156863, 0.294117659 }
                            { 0.13034986, 0.127950788, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Perks/Styles/Sorcery/ArcaneComet/Particles/Perks_Meteor_Simple_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1.5, 0 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Yasuo_Comet_Mult.TFT_ArenaSkin_Odyssey.dds"
                emitterUvScrollRateMult: vec2 = { -1, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "dustyTrail1"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 40, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 10000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 2000, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.509803951, 0.894117653, 1, 0 }
                            { 0.469993144, 0.800000012, 1, 1 }
                            { 0.329411775, 0.529411793, 1, 1 }
                            { 0.266666681, 0.31764707, 0.992156863, 0.294117659 }
                            { 0.203921571, 0.203921571, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Perks/Styles/Sorcery/ArcaneComet/Particles/Perks_Meteor_Simple_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -1.5, 0 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Yasuo_Comet_Mult.TFT_ArenaSkin_Odyssey.dds"
                emitterUvScrollRateMult: vec2 = { -1, 0 }
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_ShootingStar_Child"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar_Child"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_common_shootingstar"
        flags: u8 = 197
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Drops" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Leaves"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 30, -50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, -50, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 2, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, -2, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 300, 0, 150 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 300, 0, 150 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Yasuo_Leaf_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.666666985, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 200 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.699999988, 0.699999988, 0.699999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Yasuo_Leaves_2x2.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Motes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 30, -50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, -50, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 2, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, -2, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 300, 0, 150 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 300, 0, 150 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.666666985, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 200 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1.79999995, 1.79999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 1.79999995, 1.79999995 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.699999988, 0.699999988, 0.699999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/HA_PoroRay_snow_glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Tree_Drops"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Drops"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_trees_wind"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                emitterName: string = "Basic"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.917647004, 0, 0.572548985 }
                            { 0.372548997, 0.066666998, 0.0980390012, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Lucian/Skins/Skin07/Particles/Lucian_Skin07_Mult_min_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 270, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 0.649999976, 1.25, 0 }
                            { 0.150000006, 0.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Lucian/Skins/Skin07/Particles/Lucian_Skin07_Flame_01.dds"
                texAddressModeBase: u8 = 2
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 2, 2 }
                            { 0.5, 0.5 }
                        }
                    }
                }
                uvTransformCenter: vec2 = { 0.5, 1 }
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "candleFlickerGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.190005347, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.21360153
                            0.404214561
                            0.649425268
                            0.729885042
                            0.835249066
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.829999208, 0.190005347, 0 }
                            { 1, 0.829999208, 0.190005332, 0.300007641 }
                            { 1, 0.829999208, 0.190005347, 0.203888685 }
                            { 1, 0.829999208, 0.190005347, 0.247579113 }
                            { 1, 0.829999208, 0.190005347, 0.14563477 }
                            { 1, 0.829999208, 0.190005347, 0.247579113 }
                            { 1, 0.829999208, 0.190005347, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 150, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 150, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "candleConstantGlow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.489997715, 0.0399938971, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.489997715, 0.0399938971, 0 }
                            { 1, 0.489997715, 0.0399938971, 0.300007641 }
                            { 1, 0.489997715, 0.0399938971, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -1 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Candle"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship_Child"
                        }
                    }
                }
                emitterName: string = "shipParent"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.150000006, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 4000, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 1, 0, 0 }
                    }
                }
                blendMode: u8 = 1
                pass: i16 = -5
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 10, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/disc32.TFT_Set4.DDS"
            }
        }
        visibilityRadius: f32 = 10000
        particleName: string = "TFT_Odyssey_Yasuo_Ship"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_C_Shimmer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0379999988
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowBright"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_C_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "treeGlowConstant"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_C_Shimmer_Mesh.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/Base_SmokeErode.TFT_Set4_Act2.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Trees_RainbowMult.TFT_ArenaSkin_Odyssey_Polish.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0299999993 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Tree_Shimmer.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Tree_C_Shimmer"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_C_Shimmer"
    }
    "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 0, 20 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectRadius: f32 = 0.00499999989
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 0, 1, 0.749019623, 0.600000024 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { 1, 1 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Qbv2_Gold.TFT_ArenaSkin_Odyssey.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0.590005338, 0.319996953, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "blendCylinder"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_SharedDraft_Cylinder.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.576470613, 1, 0.776470602, 0 }
                            { 0.278431386, 1, 0.580392182, 1 }
                            { 0, 0.674509823, 0.709803939, 0 }
                        }
                    }
                }
                pass: i16 = -2
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                disableBackfaceCull: bool = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.300000012, 3.5, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Base_UnderGlow.TFT_Set3.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.5 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Base_Smoke_Erode.TFT_Set3.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 2 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "blueFire"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -1
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    45
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.380392164, 1, 0.627451003, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.377408683, 1, 0.228835061, 0 }
                            { 0.380392164, 0.941176474, 0.0713571683, 0.501960814 }
                            { 0, 0.450980395, 0.627451003, 0.501960814 }
                            { 0, 0.31764707, 0.627451003, 0 }
                        }
                    }
                }
                pass: i16 = 51
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_SmokeErode.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "thrusterGlow"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.829999208, 1, 0.349996179, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.829999208, 1, 0.349996179, 0 }
                            { 0.829999208, 1, 0.349996179, 0.600000024 }
                            { 0.829999208, 1, 0.349996179, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 150, 50 }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Yasuo_Tree_Jets"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_yasuo_tree_drones"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Malphite/TFT_Odyssey_Malphite_Candle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                emitterName: string = "Basic"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 0.917647004, 0, 0.572548985 }
                            { 0.372548997, 0.066666998, 0.0980390012, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Lucian/Skins/Skin07/Particles/Lucian_Skin07_Mult_min_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -5 }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 270, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 0.649999976, 1.25, 0 }
                            { 0.150000006, 0.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Lucian/Skins/Skin07/Particles/Lucian_Skin07_Flame_01.dds"
                texAddressModeBase: u8 = 2
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 2, 2 }
                            { 0.5, 0.5 }
                        }
                    }
                }
                uvTransformCenter: vec2 = { 0.5, 1 }
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "candleFlickerGlow"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.190005347, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.21360153
                            0.404214561
                            0.649425268
                            0.729885042
                            0.835249066
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.829999208, 0.190005347, 0 }
                            { 1, 0.829999208, 0.190005332, 0.300007641 }
                            { 1, 0.829999208, 0.190005347, 0.203888685 }
                            { 1, 0.829999208, 0.190005347, 0.247579113 }
                            { 1, 0.829999208, 0.190005347, 0.14563477 }
                            { 1, 0.829999208, 0.190005347, 0.247579113 }
                            { 1, 0.829999208, 0.190005347, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 150, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "candleConstantGlow"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.489997715, 0.0399938971, 0.209994659 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.489997715, 0.0399938971, 0 }
                            { 1, 0.489997715, 0.0399938971, 0.209994659 }
                            { 1, 0.489997715, 0.0399938971, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -3 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 150, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "candleConstantGlow1"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.345098048, 0.0431372561, 0.117647059 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.345098048, 0.0431372561, 0 }
                            { 1, 0.345098048, 0.0431372561, 0.117647059 }
                            { 1, 0.345098048, 0.0431372561, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -250 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 150, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Malphite_Candle"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Malphite/TFT_Odyssey_Malphite_Candle"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "screenMeshAlpha"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349996179, 1, 0.930006862, 0.800000012 }
                }
                pass: i16 = -1
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.5, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Pixels.TFT_ArenaSkin_Odyssey.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Static.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.0500000007 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "screenMeshAdd"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.525490224, 1, 0.898039222, 1 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.5, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Pixels.TFT_ArenaSkin_Odyssey.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Static.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.0199999996 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "screenTechHud"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.525490224, 1, 0.898039222, 1 }
                }
                pass: i16 = -1
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.699999988, 0.600000024, 0.600000024 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Tech_HudFrame.TFT_ArenaSkin_Odyssey.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0529999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.0529999994
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "screenMeshAddFlicker"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Screen_Mesh.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.525490224, 1, 0.898039222, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0919540226
                            0.0919540226
                            0.101532564
                            0.101532564
                            0.124521069
                            0.124521069
                            0.258620679
                            0.262452096
                            0.312260538
                            0.312260538
                            0.375478923
                            0.375478923
                            0.496168584
                            0.515325665
                            0.557471275
                            0.557471275
                            0.680076599
                            0.680076599
                            0.703065157
                            0.703065157
                            0.727969348
                            0.735632181
                            0.78927201
                            0.78927201
                            0.827586234
                            0.827586234
                            0.936781585
                            0.938697338
                            1
                        }
                        values: list[vec4] = {
                            { 0.525490224, 1, 0.898039222, 0 }
                            { 0.525490224, 1, 0.898039222, 0 }
                            { 0.525490224, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 1 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 0.990291238 }
                            { 0.525490165, 0.99999994, 0.898039162, 0.990291238 }
                            { 0.525490165, 0.99999994, 0.898039162, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 1 }
                            { 0.525490165, 0.99999994, 0.898039162, 1 }
                            { 0.525490165, 0.99999994, 0.898039162, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 1 }
                            { 0.525490165, 0.99999994, 0.898039162, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 0.990291238 }
                            { 0.525490165, 0.99999994, 0.898039162, 0 }
                            { 0.525490165, 0.99999994, 0.898039162, 1 }
                            { 0.525490224, 1, 0.898039222, 1 }
                            { 0.525490224, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 0 }
                            { 0.525490165, 1, 0.898039222, 0.980582535 }
                            { 0.525490224, 1, 0.898039222, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.5, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Pixels.TFT_ArenaSkin_Odyssey.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
                texDiv: vec2 = { 2, 2 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 180
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_Static.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.0199999996 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_Screens"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
    }
    "Maps/Particles/TFT/Odyssey/Common/TFT_Audio-Emitter_Odyssey_Amb_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Odyssey_Amb_Loop"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Common/TFT_Audio-Emitter_Odyssey_Amb_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_common_shootingstar"
    }
    0x0a41a344 = MapPointLightType {
        lightColor: vec4 = { 0, 1, 0.784313738, 1 }
        radius: f32 = 950
        specular: bool = false
    }
    0x62a42502 = MapPointLightType {
        lightColor: vec4 = { 0.494117647, 0.917647064, 0.921568632, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x17bdecb5 = MapPointLightType {
        lightColor: vec4 = { 0.686274529, 0.36470589, 0.611764729, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x52248cce = MapPointLightType {
        lightColor: vec4 = { 0.690196097, 0.227450982, 0.772549033, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0xafadfc34 = MapPointLightType {
        lightColor: vec4 = { 1, 0.58431375, 0, 1 }
        radius: f32 = 941
        Impact: i32 = 1
    }
    0xfd78c09d = MapPointLightType {
        lightColor: vec4 = { 0, 0.172549024, 0.384313732, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
    }
    0x2569c431 = MapPointLightType {
        lightColor: vec4 = { 1, 0.282352954, 0, 1 }
        radius: f32 = 6000
        Impact: i32 = 1
    }
    0x31141fe3 = MapPointLightType {
        lightColor: vec4 = { 0.411764711, 0.823529422, 0.764705896, 1 }
        radius: f32 = 950
        specular: bool = false
    }
    0x4c27047a = MapPointLightType {
        lightColor: vec4 = { 0.494117647, 0.866666675, 0.741176486, 1 }
        radius: f32 = 650
        specular: bool = false
        Impact: i32 = 1
    }
    0x534460ea = MapPointLightType {
        lightColor: vec4 = { 0.866666675, 0.80392158, 0.443137258, 1 }
        specular: bool = false
        Impact: i32 = 1
    }
    0x55ee3022 = MapPointLightType {
        lightColor: vec4 = { 0.70588237, 0.498039216, 0.0745098069, 1 }
        radius: f32 = 700
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x7ec5340e = MapPointLightType {
        lightColor: vec4 = { 0.0509803928, 0.0862745121, 0.0980392173, 1 }
        radius: f32 = 3000
    }
    0xdc31003a = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.717647076, 0.823529422, 1 }
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe6a78bd9 = null
            0x9080d11b = null
            0x27e0adec = null
            0x5b9cf21d = null
            0x0c413543 = null
            0xa68d8a37 = null
            0x2e833675 = null
            0xf579e674 = null
            0xf7bedb85 = null
            0xaaf93894 = null
            0x47a6df13 = null
            0xfd3964db = null
            0x0e49f39d = null
            0x4b0da566 = null
            0xd17440b7 = null
            0xf6bd0218 = null
            0x3d50c268 = null
            0x49528e83 = null
            0xa2b6f4a5 = null
            0x0ff9b414 = null
            0xce101411 = null
            0x89c5a8d3 = null
            0xcd836ec8 = null
            0xace6f95f = null
            0x3c972a91 = null
            0xf4b413bb = null
            0x0793063d = null
            0xa82f3878 = MapGroup {
                members: list2[string] = {
                    "fcba442f-4025-4700-ba70-6d7454f4ea32"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    2657.81104, -219.856415, 4405.47168, 1
                }
                name: string = "group5"
            }
            0x5a774d2e = MapGroup {
                members: list2[string] = {
                    "f77562dc-1623-40cd-8aec-9693d51f5541"
                    "5476be88-664b-4a46-8244-e339370d505a"
                    "cc4e825e-21bf-4404-b5bd-3e785fefbd4b"
                    "1bc143be-70f9-4de4-8bcf-706549add74c"
                    "1b0c9d8d-214a-45a0-a27c-8e480ea79129"
                    "c85b2ddd-54c3-4106-b336-eadde9ec1e50"
                    "0838e970-5abd-434d-ad79-acb5e8b9f052"
                    "d498167d-11be-4d69-968f-4fa0bc8522f0"
                    "c9383334-89b1-4706-b557-89e121071da5"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1206.79529, -140.874481, 3137.64355, 1
                }
                name: string = "group6"
            }
            0x201bcd18 = null
            0xd4f06c96 = null
            0xb36ea452 = null
            0x6c99e42a = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1039.13831, 15.3894711, 2041.48511, 1
                }
                name: string = "group7"
            }
            0x3bd0d109 = null
            0xfbc17ea8 = null
            0xb22b778c = null
            0xd9a439bb = MapGroup {
                members: list2[string] = {
                    "c8b49c9a-7725-44a4-80ab-d3e49f5c5b00"
                }
                transform: mtx44 = {
                    2.01565146, 0, 0, 0
                    0, 2.01565146, 0, 0
                    0, 0, 2.01565146, 0
                    2924.59839, 19.8887558, 3101.41602, 1
                }
                name: string = "group8"
            }
            0xd74e3d81 = null
            0xca899918 = null
            0x5638e26a = MapGroup {
                transform: mtx44 = {
                    0.780005276, 0, 0, 0
                    0, 0.780005276, 0, 0
                    0, 0, 0.780005276, 0
                    3432.7168, -0.000244140625, 1315.96899, 1
                }
                name: string = "group9"
            }
            0xa159632b = null
            0x2802277d = null
            0xf1490659 = null
            0x24e3ea2b = null
            0x97aff33c = null
            0x6b0121f4 = null
            0xaa1d69b7 = null
            0x5a09c543 = null
            0x2294cb40 = null
            0xb91b1cec = null
            0x08d2aeb5 = null
            0x59a4f7d8 = null
            0x9790c067 = MapGroup {
                members: list2[string] = {
                    "0923cbf3-06ee-44d3-9eb0-5fd0c2344207"
                    "655da7af-0907-443b-be09-f781a04153a3"
                    "3a5918d8-777b-489f-884e-cef8edf48e59"
                    "e7435f32-400f-40a8-b254-c08b5686a062"
                }
                transform: mtx44 = {
                    -5.7765579e-08, 0, -0.484572768, 0
                    0, 0.484572798, 0, 0
                    0.610278904, 0, -7.27509217e-08, 0
                    2956.42529, -73.9776611, 1418.84839, 1
                }
                name: string = "group19"
            }
            0x53547ad2 = null
            0x02aa2d5b = null
            0xe7dcd161 = null
            0xdf287778 = null
            0x713a3ddf = null
            0x37177fca = null
            0x4fa0b9b4 = null
            0x6fcccb06 = null
            0xff4cb76b = null
            0x4cfd9b0c = null
            0x386bf453 = null
            0xa0603d4a = null
            0xffd46457 = null
            0x3d9f0a1e = null
            0x497d2216 = null
            0x7f65c594 = null
            0xbbea7399 = null
            0x392acab0 = MapGroup {
                transform: mtx44 = {
                    0.710312426, 0, 0, 0
                    0, 0.710312426, 0, 0
                    0, 0, 0.710312426, 0
                    2930.74194, 32.7210922, 3098.84351, 1
                }
                name: string = "group22"
            }
            0xb94bd7d2 = MapGroup {
                members: list2[string] = {
                    "9e41ba8c-2ad2-4ac2-947b-efcdc2cd5339"
                    "e5296198-ae88-4905-af61-d2147856f2be"
                    "33aa62ab-5bd8-4ee3-859a-b19e98be42d9"
                    "21c4934b-1a66-4abd-b916-93d5784441f3"
                    "840675b6-a33b-42b6-893f-67cd893c835b"
                    "825a755f-ccdd-4fb2-9785-f18eccc2c265"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2777.92358, 2.91313171, 1113.1814, 1
                }
                name: string = "group23"
            }
            0x73e59522 = MapGroup {
                members: list2[string] = {
                    "b46d69bb-9c54-422a-a1e5-1d6d3e226046"
                    "2b5aa50e-5d09-47a1-9481-c40895fca5d6"
                    "829e24ca-cfed-4781-9cbb-62c9696672be"
                    "d3e1be76-3302-48a3-bf4f-36f87901cfbb"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1226.32788, 2.91325378, 2920.45508, 1
                }
                name: string = "group24"
            }
            0x54c3bda2 = null
            0x335356dc = null
            0xf2085301 = null
            0xeb25cc4a = null
            0x4bff5885 = null
            0xddd873a8 = null
            0x06f77256 = MapGroup {
                transform: mtx44 = {
                    0.929213345, 0, -0.369543612, 0
                    0, 1, 0, 0
                    0.369543612, 0, 0.929213345, 0
                    437.983582, 131.717651, 2164.97827, 1
                }
                name: string = "group25"
            }
            0x4552f16f = null
            0x70b43ccc = null
            0x00b788af = null
            0x36db0a6b = null
            0x84cd5bcb = null
            0x55e3a6fc = null
            0xbf259b5b = null
            0x90b11e2f = null
            0x20d28f94 = null
            0xd69c7d9e = null
            0x814bea33 = null
            0x0a05f428 = null
            0x171f8ebe = null
            0x8f32a2d2 = null
            0x83be3641 = null
            0x94c83906 = null
            0xe93eab2a = null
            0x5cc989ef = null
            0x949d6971 = null
            0x1c73d270 = null
            0x205aa33c = null
            0x727900ce = null
            0xf605e440 = null
            0x0864f49a = null
            0x965c1533 = null
            0x7c62f590 = null
            0x81b772af = null
            0x1d098ca0 = null
            0xb593f2a2 = null
            0x9b5480ed = null
            0x0e93b711 = null
            0xd5357503 = null
            0x4816d20b = null
            0x106a91b5 = null
            0x7e59bd64 = null
            0x2ff7865a = null
            0x081c76fe = null
            0xf385a37b = MapGroup {
                members: list2[string] = {
                    "9a9685ac-9e1d-4e0b-919f-b7a1aeb2e98b"
                    "d1609fa5-57c2-41bf-a8c3-8c0a81ff7b39"
                    "5296e8d1-73ae-4f66-bf16-d896edeb96c4"
                    "4ba2f590-6271-4d42-9957-edd1a6355ced"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    763.891541, 35.4076462, 1154.60559, 1
                }
                name: string = "group27"
            }
            0x71cf3758 = null
            0x6284e01e = null
            0x97718a64 = null
            0x0a1b2f0c = MapGroup {
                transform: mtx44 = {
                    -0.990485251, -0.137497693, 0.00577523559, 0
                    -0.202974766, 1.46018934, -0.0468949117, 0
                    -0.00134578068, -0.0322859325, -0.999477804, 0
                    3021.67773, -365.680145, 963.378662, 1
                }
                name: string = "group28"
            }
            0x1962cfb4 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2585.75708, -493.622925, 938.432617, 1
                }
                name: string = "group29"
            }
            0xdb7c190a = MapGroup {
                members: list2[string] = {
                    "5b427679-b285-4413-84a3-7e1b6c12f4dd"
                    "38ef5190-ef4c-411f-ab01-6abfb5b9141d"
                    "1c7607fc-c232-451b-b77d-064ff48cb617"
                    "3f17ec91-0ce2-4cbb-aa4a-d1c4000ec4b8"
                }
                transform: mtx44 = {
                    0.998807788, -0.0488158762, 0, 0
                    0.0622040927, 1.27274024, 0, 0
                    0, 0, 1, 0
                    1129.44189, -456.438599, 922.225952, 1
                }
                name: string = "group30"
            }
            0xa375eb76 = null
            0x89e01ef7 = null
            0x221a7aae = null
            0x244bf53b = null
            0x4a3c7ca1 = null
            0xd1d26465 = null
            0x8c2835fd = null
            0x29263c62 = null
            0xbd85d0a2 = null
            0x3c72cf5f = null
            0x449cc0da = null
            0xc6e0bff8 = null
            0x698a192e = null
            0xbf171b9d = null
            0x5d48bc4f = null
            0x0b51286a = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3001.09424, -476.666779, 3152.72437, 1
                }
                name: string = "group26"
            }
            0x1546a7fb = MapGroup {
                members: list2[string] = {
                    "4c1261b4-3807-458f-8f48-c4eb165e1a7d"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1468.23779, -1522.58508, 1866.28174, 1
                }
                name: string = "group31"
            }
            0x2d4296bd = null
            0xc4c65970 = null
            0x30b84c7e = null
            0x2fc22bb2 = null
            0xdd745142 = null
            0xc8e4ed90 = null
            0x984f0bfa = null
            0x9f7f58d8 = null
            0xb2e44aa8 = null
            0xd5ab9442 = null
            0x0658d667 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Odyssey_Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2900.60547, 19.9998169, 2267.28174, 1
                }
                name: string = "GoldMineLocatorAway"
            }
            0x9b9787df = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1092.12268, 20.000061, 1776.06726, 1
                }
                name: string = "GoldMineLocator"
            }
            0x4bff90c5 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2755.60547, 0, 2945.9248, 1
                }
                name: string = "BenchAwayLocator"
            }
            0x90883f04 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1181.35583, 0, 1123.34546, 1
                }
                name: string = "BenchHomeLocator"
            }
            0x4cb64046 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3096.94604, 0, 2918.82886, 1
                }
                name: string = "ItemBenchAwayLocator"
            }
            0x1cd3dd02 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    848.316345, 0, 1094.22803, 1
                }
                name: string = "ItemBenchLocator"
            }
            0x2f580834 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1405.49829, 0, 1484.46069, 1
                }
                name: string = "BoardLocator"
            }
            0x717bb0ac = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1628.69995, 1
                }
                name: string = "Camera_Island"
            }
            0xf874b8e7 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -1, -8.74227766e-08, 0, 0
                    -8.74227766e-08, 1, -8.74227766e-08, 0
                    7.64274186e-15, -8.74227766e-08, -1, 0
                    2067, 0, 2427.01318, 1
                }
                name: string = "Camera_Flipped_Island"
            }
            0xe9d84b9b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1063.01257, 0, 1372.51892, 1
                }
                name: string = "PerchLocator"
            }
            0x58f4606b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2885.72461, 0, 2641.72803, 1
                }
                name: string = "PerchAwayLocator"
            }
            0xe1404aa4 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 0, 2000, 1
                }
                name: string = "BoardCenterLocator"
            }
            0xc723a0b3 = MapCamera {
                0x563a1941: f32 = 3700
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_PC"
            }
            0xd0ce0321 = MapCamera {
                0x563a1941: f32 = 3700
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1967, 0, 2355, 1
                }
                name: string = "Camera_TFT_IslandAway_PC"
            }
            0x7fd48cc3 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1920.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_Mobile"
            }
            0xb9b64b31 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2067, 0, 2135, 1
                }
                name: string = "Camera_TFT_IslandAway_Mobile"
            }
            0x608bfae5 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 41
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreView"
            }
            0x2e12e907 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 89.9000015
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 100, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreThumb"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Odyssey_Design_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x8d865c3b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Skybox_Odyssey_B"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1964.89526, -0.000244140625, 1993.29199, 1
                }
                name: string = "TFT_Skybox_Odyssey_B1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x8d761e00 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Smoke"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    454.974243, 275.156403, 1285.3606, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Smoke1"
            }
            0x599f13f1 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar"
                transform: mtx44 = {
                    0.97278434, 0.231712461, 0, 0
                    -0.231712461, 0.97278434, 0, 0
                    0, 0, 1, 0
                    1968.05713, 8.40783691, 1993.98267, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShootingStar1"
                0xccf79327: u8 = 126
            }
            0xa0d12cf9 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1954.50696, 12.3688965, 1968.16199, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Ship1"
                0xccf79327: u8 = 126
            }
            0x120df8e0 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Smoke"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    381.806091, 92.0553894, 2542.82373, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Smoke2"
            }
            0xa342b9f5 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog"
                transform: mtx44 = {
                    0.984860182, 0, -1.13139307, 0
                    0, 1.5, 0, 0
                    1.50852418, 0, 1.31314683, 0
                    755.482971, 161.929382, 1823.10767, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShipLightFog1"
            }
            0x3aa29746 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog"
                transform: mtx44 = {
                    0.825380743, 0, -0.87106055, 0
                    0, 1.20000005, 0, 0
                    0.87106055, 0, 0.825380743, 0
                    745.280273, 155.625122, 2501.55762, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShipLightFog2"
            }
            0x9a2d6f26 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog"
                transform: mtx44 = {
                    0.784842014, 0, -0.907757103, 0
                    0, 1.20000005, 0, 0
                    0.907757103, 0, 0.784842014, 0
                    108.800659, 155.624756, 1740.95935, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShipLightFog3"
            }
            0xcf513539 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Hangar_Volume"
                transform: mtx44 = {
                    0.959669709, -0.281129867, 0, 0
                    0.281129867, 0.959669709, 0, 0
                    0, 0, 1, 0
                    1046.64014, 601.753296, 1804.69751, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Hangar_Volume1"
            }
            0x41e5fbaf = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Drops"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3540.37549, 130.206116, 2829.44849, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Drops1"
            }
            0xf8e2d243 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Drops"
                transform: mtx44 = {
                    0.991161048, 0, 0.132673115, 0
                    0, 1, 0, 0
                    -0.132673115, 0, 0.991161048, 0
                    3264.52515, 207.053543, 1380.01636, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Drops2"
            }
            0xb097d27b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1958.36987, 85.3206482, 1987.62073, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Wind1"
            }
            0x3c5b5c3e = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2957.27661, 55.2406693, 1270.77844, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle2"
            }
            0x6683c782 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2879.84668, 44.3643723, 1346.20032, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle4"
            }
            0x3ce17d48 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    930.155334, 23.2947197, 897.965027, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle5"
            }
            0x8ecf132c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    923.283447, 38.2808838, 926.921814, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle6"
            }
            0x93816ffc = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    900.643188, 55.2855606, 912.360535, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle7"
            }
            0xc4dbbf25 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    627.983765, 33.4695778, 1299.27515, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle8"
            }
            0x10fc3be8 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2806.94214, 52.6362915, 3104.32422, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle9"
            }
            0x92923052 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Malphite/TFT_Odyssey_Malphite_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2814.79785, 66.8625793, 3133.62402, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle10"
            }
            0xd4fd9f8f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2788.61938, 82.6833572, 3131.68872, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle11"
            }
            0x30153e7c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3120.47632, 43.5282784, 3078.19385, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle12"
            }
            0xadaa83a2 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    466.527588, 199.611374, 1504.39819, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Candle1"
            }
            0xc2fcddcd = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    396.873474, 250.436005, 1373.84497, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Candle2"
            }
            0xb35d0e3f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    841.079041, 22.2973614, 891.835938, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Candle3"
            }
            0x994f6469 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    396.112518, 248.646103, 1128.66687, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Candle4"
            }
            0xe6cbb99c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1092.46558, 8.00001526, 1618.65918, 1
                }
                name: string = "TFT_GoldMine_Odyssey_Yasuo_Start1"
            }
            0x9ae256a7 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_GoldMine_Odyssey_Yasuo_Start_Away"
                transform: mtx44 = {
                    -0.99999994, 0, 8.74227766e-08, 0
                    0, 1, 0, 0
                    -8.74227766e-08, 0, -0.99999994, 0
                    2899.85522, 8.00003052, 2428.02661, 1
                }
                name: string = "TFT_GoldMine_Odyssey_Yasuo_Start_Away1"
            }
            0xd50b77f3 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    0.767619729, 0, 0.640905559, 0
                    0, 1, 0, 0
                    -0.640905559, 0, 0.767619729, 0
                    443.679077, 196.794159, 1000.02094, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle13"
            }
            0x969b824b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShipLightFog"
                transform: mtx44 = {
                    -0.0256538671, -1.45913041, -1.36758196, 0
                    -0.183156118, 1.36366045, -1.45151067, 0
                    1.9914304, 0.10662207, -0.151115909, 0
                    389.97818, 630.919495, 3114.68628, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShipLightFog4"
            }
            0xc3f6af1b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_A_Shimmer"
                transform: mtx44 = {
                    -0.684316456, 0.29332906, -0.292694807, 0
                    0.279439986, 0.734299898, 0.0825654417, 0
                    0.283795148, -0.030011557, -0.693585575, 0
                    3249.88525, 229.628616, 1343.83936, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_A_Shimmer1"
            }
            0xbad443f3 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_C_Shimmer"
                transform: mtx44 = {
                    0.862542629, 0, 0.505984545, 0
                    0, 1, 0, 0
                    -0.505984545, 0, 0.862542629, 0
                    3544.11157, 167.260193, 2815.69434, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_C_Shimmer1"
            }
            0x17843d7b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer"
                transform: mtx44 = {
                    0.349918455, -0.00743525755, -0.00133458991, 0
                    0.00743969902, 0.349918991, 0.00116163713, 0
                    0.00130960438, -0.00118973665, 0.349995553, 0
                    3289.56445, 196.247437, 2999.19702, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_B_Shimmer1"
            }
            0xe2ba1c36 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.975564182, 0, 0.219718546, 0
                    0.134790987, -0.789717138, -0.598480284, 0
                    0.173515499, 0.613471091, -0.770419955, 0
                    3486.34619, -150.852493, 1332.2406, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets1"
            }
            0xaca0c56b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.81741333, -0.574227929, 0.0458138734, 0
                    -0.493374377, -0.73892808, -0.458876282, 0
                    0.29735291, 0.352487475, -0.887318969, 0
                    3350.37671, -157.068207, 1379.82617, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets2"
            }
            0x530ff120 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.383320063, -0.642815173, -0.663215518, 0
                    -0.652938306, -0.696467757, 0.29766503, 0
                    -0.653252006, 0.31893754, -0.686689198, 0
                    3335.90454, -131.69223, 1521.59521, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets3"
            }
            0x6c26950c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.975564182, 0, 0.219718546, 0
                    -0.134272665, -0.791544199, 0.596179187, 0
                    0.173916996, -0.61111182, -0.772202134, 0
                    3447.03101, -143.419891, 1620.30603, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets4"
            }
            0x3579ba3e = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.770162404, 0.62838155, 0.109488711, 0
                    0.485727221, -0.689036965, 0.537864089, 0
                    0.413425803, -0.361060411, -0.835892439, 0
                    3573.50513, -138.920105, 1556.09827, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets5"
            }
            0x2ba3ef77 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.639597476, 0.379807413, 0.668328345, 0
                    0.65475589, -0.724685073, -0.21477285, 0
                    0.402755231, 0.57495904, -0.712187767, 0
                    3597.73877, -160.594666, 1414.55786, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets6"
            }
            0x18d2b048 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, -0.789717138, -0.613471091, 0
                    0, 0.613471091, -0.789717138, 0
                    3558.28467, -238.90303, 2554.30225, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets7"
            }
            0x5128f723 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.810660064, -0.574227929, -0.114422515, 0
                    -0.573367, -0.73892808, -0.353886187, 0
                    0.118661359, 0.352487475, -0.92826277, 0
                    3397.83911, -240.944321, 2642.5061, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets8"
            }
            0x034b50fc = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.347990185, -0.642815173, -0.682415843, 0
                    -0.63641876, -0.696467757, 0.33151722, 0
                    -0.688384891, 0.31893754, -0.651463628, 0
                    3390.89136, -243.212677, 2833.13135, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets9"
            }
            0x7c1d15fd = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, -0.791544199, 0.61111182, 0
                    0, -0.61111182, -0.791544199, 0
                    3555.98999, -241.550766, 2924.18677, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets10"
            }
            0xf2475b91 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.770811081, 0.379807413, 0.511465073, 0
                    0.591565669, -0.724685073, -0.353386045, 0
                    0.236432448, 0.57495904, -0.78327626, 0
                    3720.68945, -245.012161, 2640.33936, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets11"
            }
            0x1ecaf010 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_Jets"
                transform: mtx44 = {
                    0.772109449, 0.62838155, -0.0947824121, 0
                    0.609000802, -0.689036965, 0.392868936, 0
                    0.181563035, -0.361060411, -0.914696753, 0
                    3725.1311, -247.324356, 2837.01074, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_Jets12"
            }
            0x1e22503f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Candle"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2931.42578, 46.5428009, 1455.23889, 1
                }
                name: string = "TFT_Odyssey_Malphite_Candle14"
            }
            0x84501be8 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer"
                transform: mtx44 = {
                    -0.220523804, 0, 0.0752213597, 0
                    0, 0.200000003, 0, 0
                    -0.0645677, 0, -0.189290836, 0
                    550.558777, 165.144669, 937.200745, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_B_Shimmer2"
            }
            0x05b26d2a = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer"
                transform: mtx44 = {
                    0.193898767, 0, -0.0665452257, 0
                    0, 0.200000003, 0, 0
                    0.0649221763, 0, 0.189169526, 0
                    553.069824, 143.941238, 1557.69897, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_B_Shimmer3"
            }
            0x9b96dd94 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Door_Dust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    366.330261, 394.365356, 2941.38086, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Door_Dust1"
            }
            0x7d9758f2 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 0.969403028, 0.245474592, 0
                    0, -0.245474592, 0.969403028, 0
                    932.780884, 104.871536, 1441.16333, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens1"
            }
            0x48af1974 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -8.74227766e-08, 0, 0.99999994, 0
                    -0.245476574, 0.969402552, -2.14602451e-08, 0
                    -0.969402492, -0.245476589, -8.47478603e-08, 0
                    781.622131, 114.443039, 1331.91809, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens2"
            }
            0x62fa387f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -6.11760242e-08, -1.56127167e-09, 0.699999928, 0
                    -0.216102973, 0.77025944, -1.71681958e-08, 0
                    -0.962824166, -0.270128727, -8.47478603e-08, 0
                    777.289673, 90.7196045, 1161.2699, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens3"
            }
            0xcd6df80f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_01"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, -8.74227766e-08, 0.99999994, 0
                    0, -0.99999994, -8.74227766e-08, 0
                    930.952759, -966.610046, 4656.52051, 1
                }
                name: string = "TFT_Odyssey_Yasuo_JetThruster_01_1"
            }
            0x3412602e = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_JetThruster_02"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, -8.74227766e-08, 0.99999994, 0
                    0, -0.99999994, -8.74227766e-08, 0
                    1305.66357, -1367.19019, 4925.14746, 1
                }
                name: string = "TFT_Odyssey_Yasuo_JetThruster_02_1"
            }
            0x670ff16a = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Space_Mist"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2400.02295, -1710, 89, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Space_Mist1"
            }
            0x8d57fa46 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Tree_B_Shimmer"
                transform: mtx44 = {
                    0.428961754, 0.135420442, -0.096195057, 0
                    -0.108909689, 0.460234106, 0.162244454, 0
                    0.132486969, -0.118240014, 0.424342811, 0
                    3332.56689, 221.30629, 1480.28577, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Tree_B_Shimmer4"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf73b1e1f = MapLightingVolume {
                sunColor: vec4 = { 0.286274523, 0.309803933, 0.43921569, 1 }
                sunDirection: vec3 = { 0.25, 0.827000022, 0.300000012 }
                0xd8851203: f32 = 75
                0xba02f116: f32 = 0.150000006
                skyLightColor: vec4 = { 0.556862772, 0.541176498, 0.345098048, 1 }
                horizonColor: vec4 = { 0.360784322, 0.447058827, 0.580392182, 1 }
                groundColor: vec4 = { 0.427450985, 0.345098048, 0.556862772, 1 }
                skyLightScale: f32 = 0.5
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.20784314, 0.454901963, 0.600000024, 1 }
                fogAlternateColor: vec4 = { 0.172549024, 0.117647059, 0.250980407, 1 }
                fogStartAndEnd: vec2 = { 500, -1500 }
                transform: mtx44 = {
                    3406.6084, 0, 0, 0
                    0, 5183.96924, 0, 0
                    0, 0, 3702.83521, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xd9d4ffc6 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Common/TFT_Audio-Emitter_Odyssey_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1990.50024, 0.000244140625, 2112.25635, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Amb_Loop1"
            }
            0x15edcb72 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Station_Amb"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    498.532104, 352.818359, 1882.27295, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Station_Amb1"
            }
            0x62c1ae3c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Amb2D"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2062.91894, -0.000122070312, 1963.30713, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Amb2D1"
            }
            0x411a4926 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_B_Drones"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1016.0343, 419.851746, 2479.57666, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_B_Drones1"
            }
            0x958b9ed5 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_A_Drones"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    688.754028, 341.396606, 1194.86011, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Yasuo_Lanterns_A_Drones1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Yasuo" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xbe6eb11d = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.0900146663
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    899.567566, 256.133759, 633.283936, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire1"
            }
            0x3a32b1da = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.122087531
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    874.494507, 493.347321, 2332.021, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire3"
            }
            0x57fe63e2 = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.0900146589
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    614.906799, 393.277557, 2636.82764, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire4"
            }
            0x1d6fb28d = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.0900146663
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    382.352051, 492.924469, 999.948425, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire5"
            }
            0xc62f5226 = MapPointLight {
                type: link = 0x7ec5340e
                radiusScale: f32 = 0.467663735
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1958.81396, 596.128784, 1996.10498, 1
                }
                name: string = "Light_Point_AmbientSurface_DragonOcean1"
            }
            0x103b033b = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 1.49265122
                intensityScale: f32 = 1.39999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1958.81396, 614.630676, 1996.10498, 1
                }
                name: string = "Freljord_FG_Center1"
            }
            0x685faeee = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 0.543674529
                intensityScale: f32 = 1.39999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    758.5, 126.155594, 1861.59302, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth1"
            }
            0x63617376 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 0.397743225
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    818.052917, 144.396881, 2466.22998, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth2"
            }
            0xc3c53db8 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 0.397743225
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    164.71405, 151.058456, 1736.27856, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth3"
            }
            0x3d1ba630 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 1.46919012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1808.99683, 809.298401, 1101.52026, 1
                }
                name: string = "Light_AV_Warm_Highlight1"
            }
            0xa5be0f54 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 1.45783329
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1808.99683, 809.298401, 2978.94214, 1
                }
                name: string = "Light_AV_Warm_Highlight2"
            }
            0x9284dc96 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 1.3993454
                intensityScale: f32 = 1.35000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3557.68433, 680.793457, 1981.0752, 1
                }
                name: string = "Freljord_FG_Torch2"
            }
            0x589232d1 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 1.15694582
                intensityScale: f32 = 1.35000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3561.11816, 726.392517, 1986.24792, 1
                }
                name: string = "Freljord_FG_Ice_Fill1"
            }
            0x5398279f = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 1.03315115
                intensityScale: f32 = 1.45000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3008.52002, 478.159119, 2704.75708, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth4"
            }
            0x37a90eed = MapPointLight {
                type: link = 0x31141fe3
                radiusScale: f32 = 0.981802285
                intensityScale: f32 = 1.85000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1616.20886, -156.980255, 257.054382, 1
                }
                name: string = "Light_Orange_01_5"
            }
            0x6c282ced = MapPointLight {
                type: link = 0x31141fe3
                radiusScale: f32 = 0.981802285
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2855.61719, -156.980255, 257.054382, 1
                }
                name: string = "Light_Orange_01_6"
            }
            0x7608251a = MapPointLight {
                type: link = 0x31141fe3
                radiusScale: f32 = 1.12278295
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2418.2019, -156.980255, 3937.84766, 1
                }
                name: string = "Light_Orange_01_7"
            }
            0x9bd6fdb2 = MapPointLight {
                type: link = 0x4c27047a
                intensityScale: f32 = 0.449999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3634.20654, -127.977722, 2301.26489, 1
                }
                name: string = "Light_Green_01_1"
            }
            0x4b74cdb3 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 0.933993638
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    322.245392, 192.85495, 3205.31152, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth6"
            }
            0xba49279e = MapPointLight {
                type: link = 0x4c27047a
                radiusScale: f32 = 0.135651723
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2826.31616, 150.098618, 3150.2395, 1
                }
                name: string = "Light_Green_01_2"
            }
            0xc4924dc3 = MapPointLight {
                type: link = 0x4c27047a
                radiusScale: f32 = 0.135651723
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2943.60815, 133.687851, 3150.5769, 1
                }
                name: string = "Light_Green_01_3"
            }
            0x8989f34e = MapPointLight {
                type: link = 0x4c27047a
                radiusScale: f32 = 0.135651723
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2826.31616, 150.098618, 3180.96191, 1
                }
                name: string = "Light_Green_01_4"
            }
            0x2ede8027 = MapPointLight {
                type: link = 0x4c27047a
                radiusScale: f32 = 0.135651723
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2943.60815, 133.687851, 3181.29932, 1
                }
                name: string = "Light_Green_01_5"
            }
            0xb3527f84 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.509662807
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    893.267883, 99.6013031, 911.718933, 1
                }
                name: string = "Light_Red_01_1"
            }
            0x5212fb2d = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.387901008
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    630.877869, 71.3108521, 1301.3866, 1
                }
                name: string = "Light_Red_01_2"
            }
            0x16333346 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2922.35327, 194.772583, 1262.22327, 1
                }
                name: string = "Light_Red_01_3"
            }
            0xc915e09f = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.407857597
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2803.07642, 121.909805, 3119.47729, 1
                }
                name: string = "Light_Red_01_4"
            }
            0x96ff0a63 = MapPointLight {
                type: link = 0x31141fe3
                radiusScale: f32 = 0.211220011
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1086.41064, 23.2220345, 2761.36743, 1
                }
                name: string = "Light_Orange_01_9"
            }
            0xc27e9b86 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.569893003
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    457.516083, 197.359451, 2137.66357, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean1"
            }
            0xa61f1347 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1795.28369, -1436.86951, 1310.68945, 1
                }
                name: string = "Odyssey_LightTeal_Fill5"
            }
            0x0ae68e92 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1724.16675, -1113.47046, 1310.68945, 1
                }
                name: string = "Odyssey_LightTeal_Fill6"
            }
            0x580aab02 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1417.79785, -1182.17944, 1310.68945, 1
                }
                name: string = "Odyssey_LightTeal_Fill7"
            }
            0x8c3fc695 = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.0998023301
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    548.681824, 267.572205, 1251.51599, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire6"
            }
            0x9abaabed = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.387901008
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    444.514069, 221.50975, 999.558655, 1
                }
                name: string = "Light_Red_01_6"
            }
            0x2d8b1601 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.387901008
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    467.029358, 221.50975, 1505.20349, 1
                }
                name: string = "Light_Red_01_7"
            }
            0x551a9019 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.387901008
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    395.66864, 266.004181, 1373.67578, 1
                }
                name: string = "Light_Red_01_8"
            }
            0x092cb5b9 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.387901008
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    395.998322, 266.004181, 1128.42993, 1
                }
                name: string = "Light_Red_01_9"
            }
            0xd5df9bf2 = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.0998023301
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    322.244995, 192.854996, 3205.31201, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire8"
            }
            0xc7997036 = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.3274571
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    914.46991, 142.771851, 1285.39673, 1
                }
                name: string = "Odyssey_LightBlue_Fill1"
            }
            0x8bd39338 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2834.05103, 194.772583, 1364.46765, 1
                }
                name: string = "Light_Red_01_10"
            }
            0xf0cdefaf = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2910.67188, 194.772583, 1494.68738, 1
                }
                name: string = "Light_Red_01_11"
            }
            0x3973db86 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1488.46631, -1495.0238, 1310.68945, 1
                }
                name: string = "Odyssey_LightTeal_Fill1"
            }
            0xe425cea9 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1411.78967, -1086.60791, 2655.06201, 1
                }
                name: string = "Odyssey_LightTeal_Fill2"
            }
            0x05ad6856 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1761.47156, -1151.0531, 2655.06201, 1
                }
                name: string = "Odyssey_LightTeal_Fill3"
            }
            0x899d4e35 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1679.32776, -1482.94177, 2655.06201, 1
                }
                name: string = "Odyssey_LightTeal_Fill4"
            }
            0x7240d169 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1341.6239, -1409.00183, 2655.06201, 1
                }
                name: string = "Odyssey_LightTeal_Fill8"
            }
            0xd85eee5c = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 0.349999994
                intensityScale: f32 = 2
                overrideCastStaticShadows: option[bool] = {
                    false
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    591.245972, 332.830597, 1943.53247, 1
                }
                name: string = "Light_Red_01_5"
            }
            0xca8f722a = MapPointLight {
                type: link = 0x2569c431
                radiusScale: f32 = 0.122087531
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2930.95532, 374.13089, 971.002441, 1
                }
                name: string = "Light_CenterAlt_Point_DragonFire2"
            }
            0x56064ce2 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 1.20863271
                intensityScale: f32 = 1.39999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1435.38086, -468.138611, 4643.01953, 1
                }
                name: string = "Freljord_FG_Torch1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Yasuo"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x33a5be05 = MapGroup {
                members: list2[string] = {
                    "099d03c5-d97d-4b75-9dd8-46b5cd2f53b6"
                    "e1a4e992-1951-4dbf-94bd-2d2fea6894d6"
                    "f026ca2b-60b8-4ac4-9f6a-7dd982ee3244"
                    "94bcd601-85ee-48ea-98b7-9dd382c335e9"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1872.98828, 0.4328022, 2922.78638, 1
                }
                name: string = "group1"
            }
            0x7ae527cc = MapGroup {
                members: list2[string] = {
                    "3d69b88d-8d3f-4055-b931-ba2d955e6a35"
                }
                transform: mtx44 = {
                    0.941365361, 0, -0.337388873, 0
                    0, 1, 0, 0
                    0.337388873, 0, 0.941365361, 0
                    591.352905, 364.265289, 2690.17725, 1
                }
                name: string = "group2"
            }
            0xe7cf11da = MapGroup {
                members: list2[string] = {
                    "f41a4aa2-0ac9-478a-aca9-0d8b69885440"
                    "7a288144-81f1-4f95-ad40-1139fd022255"
                    "2576000a-16f0-4e3e-877f-7bdbb2b898d9"
                    "2080fa32-7828-4bce-9b02-fa7b98713cca"
                    "2cf781f7-7916-472e-9d62-5c9aa5715f2e"
                    "de78137e-1f92-4bc4-ba76-37351ad0be2f"
                    "697067dd-e05a-4e91-9837-91be77b1f45c"
                    "f2ee3e42-05b0-45df-890b-714a6b26d041"
                    "fe299622-33d9-455e-b475-1ff4bd2d000f"
                    "374f35bd-52aa-4f45-a59f-14152aa01366"
                    "4451df45-a245-4e09-a5cc-781f4023fedd"
                    "b837b538-c708-4594-8ced-8f99286fab5f"
                }
                transform: mtx44 = {
                    0.0104777087, 0, -0.999945045, 0
                    0, 1, 0, 0
                    0.999945045, 0, 0.0104777087, 0
                    -95.5206604, -16.7783508, 1425.33997, 1
                }
                name: string = "group3"
            }
            0xb59844c3 = MapGroup {
                members: list2[string] = {
                    "8af4623d-fe16-47cb-b120-da3bed09e17a"
                    "2c60f709-bff5-4846-902c-b35f5ab0e9f5"
                    "efd33308-737b-41b2-ac8c-402d057d6272"
                    "652b245f-ce68-4c72-b270-ac0a64fc32ac"
                    "214a53ba-c3d0-4787-bdb0-dc7e3edfeb78"
                    "8649d0ae-db0d-4cb8-b2a1-1b6f3fe4545f"
                }
                transform: mtx44 = {
                    0.0104777087, 0, -0.999945045, 0
                    0, 1, 0, 0
                    0.999945045, 0, 0.0104777087, 0
                    -95.5206604, -16.7783508, 1970.95886, 1
                }
                name: string = "group4"
            }
            0x2e5607a8 = MapGroup {
                name: string = "group10"
            }
            0x05efa790 = MapGroup {
                name: string = "group11"
            }
            0xd7f2b0c1 = MapGroup {
                name: string = "group12"
            }
            0x9fc68527 = MapGroup {
                name: string = "group13"
            }
            0x8144c2cc = MapGroup {
                members: list2[string] = {
                    "766a4561-c9ca-445e-b1e4-69a3d4de0723"
                }
                name: string = "group14"
            }
            0xdafab73f = MapGroup {
                members: list2[string] = {
                    "7e5d8366-b304-40f3-985d-edcf8cd36c60"
                    "e1e28f90-8528-4fe4-821d-5e85799e9fe6"
                    "4f1b1310-88ba-4819-a6c3-ea5813404f04"
                    "267e8da7-7f4a-40ea-bc2b-290467352a2b"
                    "80f50b42-fa59-44b4-adb3-44a7b796b251"
                    "91243245-7c90-47c5-8c34-fda58779283f"
                    "424cd0d8-6959-4aaa-a219-6fcf9a836945"
                    "e3b6d0fd-2055-428c-8d34-f2265c3016fe"
                    "6cd71985-9396-42aa-89ac-31fc7e9909cc"
                    "503f1734-d4e7-4ef4-b1b3-47c6eb5cebe5"
                    "cd25d4bc-302a-4aa5-9561-36556e3a9ab2"
                    "30007c94-92d8-4023-8a19-3f0eec5d1a9a"
                    "7782e5da-1caf-42da-a81b-5b985f94c294"
                    "b0ddd723-80d6-44b4-8621-b78412bad88b"
                    "e05c433a-40c9-4cb0-a316-7c2f56633658"
                    "8fff079a-dff7-4c02-ae0f-876194558c81"
                    "15d5b15a-e460-4de5-b440-b97f55b8de22"
                    "bad3af90-59be-4f6d-ab14-22ecc7013e55"
                }
                name: string = "group15"
            }
            0x28978b09 = MapGroup {
                members: list2[string] = {
                    "29d3f17d-a513-409d-b82e-fe10e430de35"
                    "ca299042-7a02-42e6-afb3-5f8a8adc095f"
                }
                name: string = "group16"
            }
            0x42d2015b = MapGroup {
                members: list2[string] = {
                    "d5f1358a-2c27-4e40-ab2b-7e8d84a2924b"
                }
                name: string = "group17"
            }
            0x2dccedbd = MapGroup {
                members: list2[string] = {
                    "4d79b30e-8295-49c9-8e51-9919517b0364"
                    "1c6fd260-f0a4-4d78-8a32-03093ecc4e16"
                    "a3281f31-948e-45fd-b993-7ceae4211089"
                    "f88209bd-4216-4e86-a2a4-80913a585edb"
                    "82c8e279-b178-4667-b5c4-2f5f89fa4f84"
                    "ff1c87c9-a4c3-41c1-a1cc-1b7d6f4d6a2e"
                    "8f689755-4ddd-48a2-bc9a-bb1cdfdd1853"
                }
                name: string = "group18"
            }
            0xe7594b1b = MapGroup {
                members: list2[string] = {
                    "17fb9d93-e53b-4068-8db3-03726af35448"
                    "3ed8b713-240a-426d-8f0d-28bdeed19367"
                }
                transform: mtx44 = {
                    -5.84353188e-08, 0, -0.490190953, 0
                    0, 0.490190983, 0, 0
                    0.666705012, 0, -7.94774309e-08, 0
                    2970.46118, -77.7339935, 1485.29321, 1
                }
                name: string = "group20"
            }
            0x66696858 = null
            0x10f053f3 = null
            0x3afa1851 = null
            0x68796272 = null
            0x901926d3 = null
            0x01f346fc = null
            0x1314fd84 = null
            0x3a4c08e9 = null
            0xe44aa62e = null
            0xab9c5a71 = null
            0x44675229 = MapGroup {
                transform: mtx44 = {
                    0.569686353, 0, 0, 0
                    0, 0.569686353, 0, 0
                    0, 0, 0.569686353, 0
                    745.984497, 0, 4429.15234, 1
                }
                name: string = "group21"
            }
            0x6812a3e0 = null
            0xb8e519c2 = null
            0x8f2868b7 = null
            0x88b3fa87 = null
            0x86c4c4bc = null
            0xe1d25ba4 = null
            0x4be821d2 = null
            0x23fc5ab0 = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    2043.02392, 12.3720398, 2893.24316, 1
                }
                name: string = "group36"
            }
            0xb919c1da = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3174.62744, 84.4199829, 2818.49121, 1
                }
                name: string = "group37"
            }
            0x2387b5dc = null
            0xaf711f3d = null
            0x0d52256e = null
            0x5d645ea2 = MapGroup {
                members: list2[string] = {
                    "fc693b33-97ec-4f77-827c-40ace9eb3862"
                    "f28001f4-ac70-4173-b582-af0fb1cde8eb"
                }
                transform: mtx44 = {
                    -0.99919641, 0, -0.0400821418, 0
                    0, 1, 0, 0
                    0.0400821418, 0, -0.99919641, 0
                    1603.34241, -1297.573, 1478.06921, 1
                }
                name: string = "group41"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Odyssey_Yasuo" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Odyssey_Yasuo"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.701960802, 0.784313738, 0.839215696, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.454901963, 0.631372571, 0.741176486, 1 }
                horizonColor: vec4 = { 0.274509817, 0.419607848, 0.509803951, 1 }
                groundColor: vec4 = { 0.450980395, 0.568627477, 0.650980413, 1 }
                skyLightScale: f32 = 1.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.25
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Odyssey_Yasuo/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Odyssey_Yasuo_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            "Art_Shared" = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Shared"
            "Odyssey_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Odyssey/Odyssey_Design_Base"
            0xf4b1371e = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Yasuo"
            0x9aafd1f1 = "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Yasuo"
            0xffdf14b1 = "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Yasuo"
            0xd219434f = "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Yasuo"
            0x4a08c3d7 = "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Yasuo"
            0xe37ff9e0 = "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Yasuo"
        }
    }
}
