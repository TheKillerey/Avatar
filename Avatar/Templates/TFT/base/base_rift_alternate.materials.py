#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Materials/Base/Default/Bench_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/Bench_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Bench_A.TFTBoardSizeIncrease.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_D_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_D_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_GrassRock_C.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/Brazier_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/Brazier_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Brazier_B.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_CliffRock_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_Glow_G_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_Glow_G_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/BattleField_G.TFTBoardSizeIncrease.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/black.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Offset"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Factor"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Color"
                value: vec4 = { 0.486274511, 0.117647059, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Bounds"
                value: vec4 = { 0, 2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Frequency"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Speed"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { -0.300000012, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Frequency"
                value: vec4 = { 20, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_SmoothStep"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity_Min_Max"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Rotation"
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_DIFFUSE_COLOR"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_RADIAL_GLOW"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_UV_SCROLL_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_DIRECTION"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_AS_ALPHA"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "RADIAL_UV_LOCALSPACE_TOGGLE"
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Glow"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {}
    }
    "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_CliffRock_B.TFTBoardSizeIncrease.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_C_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/POI_Base_Rock_C_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_GrassRock_B.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_G_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_G_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/BattleField_G.TFTBoardSizeIncrease.dds"
                addressW: u32 = 1
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/Rocks_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/Rocks_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Rocks_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_Glow_Rift_Alternate_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/BattleField_Glow_Rift_Alternate_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/BattleField_G.TFTBoardSizeIncrease.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/black.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Offset"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Factor"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Color"
                value: vec4 = { 0.152941182, 0.635294139, 0.741176486, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Bounds"
                value: vec4 = { -2500, 2500, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Frequency"
                value: vec4 = { 80, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Speed"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { -0.300000012, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Frequency"
                value: vec4 = { 20, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_SmoothStep"
                value: vec4 = { -0.5, 1.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity_Min_Max"
                value: vec4 = { 0, 0.800000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Rotation"
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_DIFFUSE_COLOR"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_RADIAL_GLOW"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_UV_SCROLL_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_DIRECTION"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_AS_ALPHA"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "RADIAL_UV_LOCALSPACE_TOGGLE"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Glow"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {}
    }
    "Maps/KitPieces/TFT/Materials/Base/Default/Base_Center_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Default/Base_Center_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_GrassMain_A.TFTBoardSizeIncrease.dds"
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
    "Maps/KitPieces/TFT/Materials/Base/Alpha/Flowers_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Alpha/Flowers_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Flowers_A.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
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
    "Maps/KitPieces/TFT/Materials/Base/Alpha/WaterPlane_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Alpha/WaterPlane_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Island_Waterfall_Bkdrop_A.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
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
    "Maps/KitPieces/TFT/Materials/Base/Alpha/Roots_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Alpha/Roots_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/TFT_Roots.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
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
    "Maps/KitPieces/TFT/Materials/Base/Alpha/Grass_Edging_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/Alpha/Grass_Edging_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/Edging_Grass_A.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
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
    "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Bush_Wind_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Bush_Wind_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/TreesBrush_A.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "LS_XYZ_Offset"
                value: vec4 = { 1.5, 0.5, 1.5, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LS_Sin_Frequency"
                value: vec4 = { 55, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LS_Sin_Bounds"
                value: vec4 = { -650, 650, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LS_Sin_Time"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bend_Time"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LS_Sin_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Opacity_Clip"
                value: vec4 = { 0.800000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bend_XYZ_Offset"
                value: vec4 = { 2, 5, -2, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bend_Mask_Bounds"
                value: vec4 = { 0, 115, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bend_Mask_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LS_Offset_Global"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Offset_Global"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_SIN"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_Wind_Simple"
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Tree_Bend_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Tree_Bend_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/TreesBrush_A.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "X_Offset_Value"
                value: vec4 = { 15, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Offset_Value"
                value: vec4 = { 5, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Offset_Value"
                value: vec4 = { 10, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Mask_A_LS_Bounds"
                value: vec4 = { -150, 750, 0.5, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Mask_A_LS_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Time_Multiplier"
                value: vec4 = { 0.600000024, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Time_Multiplier"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Time_Multiplier"
                value: vec4 = { 0.800000012, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Bend_Intensity"
                value: vec4 = { 1, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Time_Offset"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Time_Offset"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Time_Offset"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Bounds"
                value: vec4 = { 0, 1000, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Frequency"
                value: vec4 = { 45, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Speed"
                value: vec4 = { 1, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_WS_Offset"
                value: vec4 = { 0.5, 0.150000006, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_WS_Offset"
                value: vec4 = { 0, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_WS_Offset"
                value: vec4 = { 0.349999994, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Shake_Intensity"
                value: vec4 = { 1, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_LS_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_RANDOM_FLOAT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_X_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Z_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_WS_SIN"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_MASTER_VIEW_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_Z_OFFSET"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_VertexBend"
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Bush_Bend_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Base/VertexAnimation/Bush_Bend_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Base/TreesBrush_A.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "X_Offset_Value"
                value: vec4 = { 6, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Offset_Value"
                value: vec4 = { 5, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Offset_Value"
                value: vec4 = { 10, 0.600000024, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Mask_A_LS_Bounds"
                value: vec4 = { 0, 250, 0.5, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Mask_A_LS_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Time_Multiplier"
                value: vec4 = { 0.600000024, 0.600000024, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Time_Multiplier"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Time_Multiplier"
                value: vec4 = { 0.800000012, 0.600000024, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Bend_Intensity"
                value: vec4 = { 0.300000012, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Time_Offset"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Time_Offset"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Time_Offset"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Bounds"
                value: vec4 = { 0, 1000, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Frequency"
                value: vec4 = { 35, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Speed"
                value: vec4 = { 1, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_WS_Offset"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_WS_Offset"
                value: vec4 = { 0.0500000007, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_WS_Offset"
                value: vec4 = { 0.300000012, 0.300000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Shake_Intensity"
                value: vec4 = { 1, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WS_Sin_Vector"
                value: vec4 = { 0, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_LS_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_RANDOM_FLOAT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_X_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Z_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_WS_SIN"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_MASTER_VIEW_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_Y_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WS_Z_OFFSET"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_VertexBend"
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/TFT_Skybox2.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/white.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Blend"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Multiply"
                value: vec4 = { 1, 1, 1, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_ROTATE_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_COLOR_BLEND"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_Skybox"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Default/Default/POI_Base_Rock_Front_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/POI_Base_Rock_Front_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/POI_Base_Rock_Front.dds"
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
    "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/TFT_Skybox_Bottom_2b.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/white.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Blend"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Multiply"
                value: vec4 = { 1, 1, 1, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_ROTATE_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_COLOR_BLEND"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_Skybox"
                        shaderMacros: map[string,string] = {
                            "NO_BAKED_LIGHTING" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Default/Default/Flowers_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/Flowers_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/Flowers_B.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
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
    "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "WaterCausticx"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 0, 15 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 120, 1, 120 }
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
                                { 120, 1, 120 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 41
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/SRU_river_watercaustics_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9000
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 2 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterCaustics_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, -0.100000001 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_River_WaterCaustics_01_Mult.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0799999982, -0.180000007 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0799999982, -0.180000007 }
                        }
                    }
                }
            }
        }
        particleName: string = "TFT_Water_WaterCaustics_B"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_B"
    }
    "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "WaterCausticx"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, -25 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 120, 1, 120 }
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
                                { 120, 1, 120 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 41
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/SRU_river_watercaustics_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 2 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterCaustics_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, -0.100000001 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_River_WaterCaustics_01_Mult.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0799999982, -0.180000007 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0799999982, -0.180000007 }
                        }
                    }
                }
            }
        }
        particleName: string = "TFT_Water_WaterCaustics_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_A"
    }
    "Maps/Particles/TFT/Base/Waterfall_Edge_Ripple_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                emitterName: string = "Shore_01"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Base_Waterfall_Edge_Ripple_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_River_Shore_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_RiverEdging_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "Shore_02"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Base_Waterfall_Edge_Ripple_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_River_Shore_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_RiverEdging_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
            }
        }
        visibilityRadius: f32 = 350
        particleName: string = "Waterfall_Edge_Ripple_A"
        particlePath: string = "Maps/Particles/TFT/Base/Waterfall_Edge_Ripple_A"
    }
    "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.29999995
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
                                    0.300000012
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
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 800
                            }
                            strength: embed = ValueFloat {
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
                                                1
                                            }
                                        }
                                    }
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0.5
                                        5
                                    }
                                }
                            }
                        }
                    }
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 50
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
                                        50
                                    }
                                }
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 5
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
                                        5
                                    }
                                }
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                    fieldOrbitalDefinitions: list[embed] = {
                        VfxFieldOrbitalDefinitionData {
                            direction: embed = ValueVector3 {
                                constantValue: vec3 = { 0.100000001, 0.300000012, 0.100000001 }
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
                                        { 0.100000001, 0.300000012, 0.100000001 }
                                    }
                                }
                            }
                        }
                    }
                }
                emitterName: string = "Basic"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 300, 50, 300 }
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
                                { 300, 50, 300 }
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.745098054, 0.454901963, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0940959379
                            0.190036908
                            0.311808109
                            0.376383752
                            0.488929898
                            0.667896688
                            0.754612565
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.00719428, 0.188191876, 0.188191876 }
                            { 0.452823341, 0.512915134, 0.512915134 }
                            { 0.876766205, 0.718312383, 0.718312383 }
                            { 0.398530096, 0.821011007, 0.821011007 }
                            { 0.856115103, 1, 1 }
                            { 0.33093524, 0.626373589, 0.626373589 }
                            { 0.625899255, 0.487179488, 0.487179488 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Firefly_Mote.TFT_Set5.dds"
            }
        }
        particleName: string = "TFT_Map_Fireflies_Dark"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Pond_Night" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Pond_Night"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Pond_Night"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_pond"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Waterfall" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Waterfall"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Waterfall"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_day_waterfall_1"
    }
    "Maps/Particles/TFT/Base/TFT_Sparks_Blue" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
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
                                    0.5
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
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Lightning_AOE_Ring"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -15, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.75
                                        1
                                    }
                                }
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
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Lighting_Cyl.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.313725501, 0.4627451, 1, 0.549019635 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.313725501, 0.4627451, 1, 0.549019635 }
                            { 0.313725501, 0.4627451, 1, 0.549019635 }
                            { 0.313725501, 0.4627451, 1, 0.290984154 }
                            { 0.313725501, 0.4627451, 1, 0.549019635 }
                            { 0.313725501, 0.4627451, 1, 0 }
                            { 0.313725501, 0.4627451, 1, 0.549019635 }
                            { 0.313725501, 0.4627451, 1, 0.549019635 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.400000006
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_LightningErosion03.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
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
                                    -360
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2000, 3000, 2000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
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
                        }
                        values: list[vec3] = {
                            { 2000, 3000, 2000 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_Lightning03.dds"
                frameRate: f32 = 5
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 4 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "Lightning_AOE_Ring1"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -65, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.75
                                        1
                                    }
                                }
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
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Lighting_Cyl.sco"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.313725501, 0.968627453, 1, 0.792156875 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                            { 0.313725501, 0.968627453, 1, 0 }
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                            { 0.313725501, 0.968627453, 1, 0.792156875 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_LightningErosion03.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
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
                                    -15
                                    15
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -15
                                    15
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2000, 2400, 2000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
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
                        }
                        values: list[vec3] = {
                            { 2000, 2400, 2000 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_Lightning03.dds"
                frameRate: f32 = 5
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 4 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2.20000005
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "Lightning_AOE_Ring2"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.75
                                        1
                                    }
                                }
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
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_R_Decal_Edge.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.396078438, 0.53725493, 1, 0.329411775 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                            { 0.396078438, 0.53725493, 1, 0 }
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                            { 0.396078438, 0.53725493, 1, 0.329411775 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_LightningErosion03.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2000, 1900, 2000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
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
                        }
                        values: list[vec3] = {
                            { 2000, 1900, 2000 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 9 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 9 }
                            { 0.899999976, 0.899999976, 9 }
                            { 0.899999976, 0.899999976, 9 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_E_Lightning03.dds"
                frameRate: f32 = 5
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 3 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
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
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "Lightning_AOE_Ring3"
                importance: u8 = 2
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.75
                                        1
                                    }
                                }
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
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_R_Decal_Edge.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.00392156886, 0.270588249, 1, 0.298039228 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.144919783
                            0.31764707
                            0.502139032
                            0.685561478
                            0.826203227
                            1
                        }
                        values: list[vec4] = {
                            { 0.00392156886, 0.270588249, 1, 0 }
                            { 0.00392156886, 0.270588249, 1, 0.0931372568 }
                            { 0.00392156886, 0.270588249, 1, 0.258455873 }
                            { 0.00392156886, 0.270588249, 1, 0.298039228 }
                            { 0.00392156886, 0.270588249, 1, 0.265441179 }
                            { 0.00392156886, 0.270588249, 1, 0.0861519575 }
                            { 0.00392156886, 0.270588249, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                                    -360
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18.5, 1, 4.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
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
                        }
                        values: list[vec3] = {
                            { 18.5, 1, 4.5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_P_Proc_Lightning_Glow.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
            }
        }
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Sparks_Blue"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Sparks_Blue"
    }
    "Maps/Particles/TFT/Base/TFT_Water_Ripple_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.30000019
                }
                emitterName: string = "Streaks2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Water_Ripples_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.482035935
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.273049653 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_River_Ripples_01.SRE_Base.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_River_Ripples_Mult_01.SRE_Base.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, -0.100000001 }
                }
            }
        }
        visibilityRadius: f32 = 650
        particleName: string = "TFT_Water_Ripple_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_Ripple_A"
    }
    "Maps/Particles/TFT/Base/TFT_Water_Ripple_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.30000019
                }
                emitterName: string = "Streaks2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Water_Ripples_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.482035935
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.109219857 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_River_Ripples_01.SRE_Base.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_River_Ripples_Mult_01.SRE_Base.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, -0.100000001 }
                }
            }
        }
        visibilityRadius: f32 = 650
        particleName: string = "TFT_Water_Ripple_B"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_Ripple_B"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Short" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Frog_Short"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Short"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_frog_short"
    }
    "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.699999988
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
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 750, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -200, 750, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
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
                                { 10, 10, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.223529413, 0.937254906, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.223529413, 0.937254906, 1, 0 }
                            { 0.223529413, 0.937254906, 1, 1 }
                            { 0.223529413, 0.937254906, 1, 0.800000012 }
                            { 0.223529413, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -180
                                    180
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
                    constantValue: vec3 = { 80, 80, 80 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 80 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.600000024, 0.600000024 }
                            { 0.5, 1, 1 }
                            { 0.300000012, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Env_MB_brazierFire_flipbook_01.TFT_1105.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Env_MB_brazierFire_mult2.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.25 }
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
                                    1
                                    -1
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDivMult: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.368627459, 0.325490206, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.368627459, 0.325490206, 1, 0 }
                            { 0.368627459, 0.325490206, 1, 1 }
                            { 0, 0.00510572875, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Varus/Skins/Base/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire1"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -200, 500, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
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
                                { 10, 10, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 4
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
                            { 1, 1, 1, 0.800000012 }
                            { 0, 0, 0.498039216, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -180
                                    180
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
                    constantValue: vec3 = { 80, 80, 80 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 80 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.600000024, 0.600000024 }
                            { 0.5, 1, 1 }
                            { 0.300000012, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbook_01.SRI_Slots.dds"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.25
                        }
                    }
                }
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -20, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 5, 5, 5 }
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
                                { 5, 5, 5 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 0.269993126, 0.269993126, 0.930006862 }
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
                            { 0.269993126, 0.269993126, 0.269993126, 0.930006862 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.0274509806, 0, 0.458823532, 0.239215687 }
                            { 0.329411775, 0, 0.992156863, 1 }
                            { 0, 0.396078438, 0.458823532, 0.450980395 }
                            { 0.113725491, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
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
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
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
                                    -80
                                    80
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
                isLocalOrientation: flag = false
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 90, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Sl_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                emitterName: string = "baseGlow1"
                blendMode: u8 = 4
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
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "baseGlow2"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.540001512 }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
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
                    10.1999998
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "ground_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.709803939, 0.129411772, 1, 1 }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "mouth_flame_R"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 40, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.620004594 }
                }
                pass: i16 = -2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 2 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 60, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks2"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
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
                            { 0.400000006, 0.400000006, 0.400000006 }
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
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, 15, 25 }
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
                                { 25, 15, 25 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0.498039216, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 0 }
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
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.TFT_Set4.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                0x538effa4: flag = true
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                period: option[f32] = {
                    4.5
                }
                timeActiveDuringPeriod: option[f32] = {
                    3
                }
                emitterName: string = "Arcs"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 30, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
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
                                { 0, 50, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
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
                pass: i16 = 30
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 360, 0 }
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
                            { 20, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 75, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499000013
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.75
                                    -1
                                    0.75
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 75, 75, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                }
                texture: string = "ASSETS/Characters/TFT_Kennen/Skins/Base/Particles/TFT_Kennen_Base_R_Electric_Arcs.dds"
                frameRate: f32 = 1
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 16
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
                            16
                        }
                    }
                }
                numFrames: u16 = 16
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 6, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    1.39999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                emitterName: string = "Black_Bits"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 70 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 0, 250, 70 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.649999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
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
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 40, 20 }
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
                                { 40, 40, 20 }
                            }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.00784313772, 0.227450982, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = -50
                colorLookUpScales: vec2 = { 0.600000024, 1 }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 12, 1, 1 }
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
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Mis_AlphaCircles.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
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
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "flash_Energy_Errode"
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
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
                            { 20, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, 0, 0 }
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
                                { 25, 0, 0 }
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
                blendMode: u8 = 4
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
                            { 0.666666687, 0, 1, 1 }
                            { 0.349019617, 0, 0.149019614, 1 }
                            { 0.333333343, 0, 0, 0 }
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
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 0
                    erosionMapName: string = "ASSETS/Shared/Particles/Base_Mis_BlastErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
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
                    constantValue: vec3 = { 60, 1.20000005, 1.20000005 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.10000002
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
                            { 60, 1.20000005, 1.20000005 }
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
                            { 0.5, 0.5, 0.5 }
                            { 1.5, 1.5, 1.5 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_ShieldFresnelRing.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.800000012
                                    1.39999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                emitterName: string = "Black_Bits1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 70 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 0, 250, 70 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.649999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, -10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 40, 20 }
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
                                { 30, 40, 20 }
                            }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.00784313772, 0.227450982, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = -1
                colorLookUpScales: vec2 = { 0.600000024, 1 }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 10
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 12, 1, 1 }
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
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Mis_AlphaCircles.dds"
            }
        }
        particleName: string = "TFT_BrazierFire_Rift_Alternate"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate"
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/Base/TFT_Water_RippleWavy_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WavyFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/SRU_river_longwhitewavyfoam_01.scb"
                    }
                }
                blendMode: u8 = 4
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_River_LongWhiteWavyFoam_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.25 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_River_LongWhiteWavyFoam_Mult_01.dds"
            }
        }
        particleName: string = "TFT_Water_RippleWavy_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_RippleWavy_A"
    }
    "Maps/Particles/TFT/Base/TFT_Waterfall_Front_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Plane_D.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.150000006 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.550000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 10, 0, 0 }
                                { 30, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_E.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, -1.20000005 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls2"
                disabled: bool = true
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                pass: i16 = 20
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_02.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_02.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.400000006, -0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "TopEdgeHightlight"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_EdgeHiLite_D.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = 30
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                textureMult: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "SideFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_SideFoam_D.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.459998488 }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.699999988 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_Mult_01.NPE_MapsMountain.dds"
            }
        }
        visibilityRadius: f32 = 2500
        particleName: string = "TFT_Waterfall_Front_B"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Waterfall_Front_B"
    }
    "Maps/Particles/TFT/Base/TFT_Waterfall_Front_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Plane_C.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.150000006 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.550000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 10, 0, 0 }
                                { 30, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_D.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, -1.20000005 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "TopEdgeHightlight"
                importance: u8 = 0
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_EdgeHiLite_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = 30
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                textureMult: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "SideFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_SideFoam_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.459998488 }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.699999988 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_Mult_01.NPE_MapsMountain.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.80000019
                }
                emitterName: string = "ShoreTop"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Shoretop_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00692840666
                            0.204291046
                            0.760950029
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.255319148 }
                            { 1, 1, 1, 0.380777866 }
                            { 1, 1, 1, 0.39579466 }
                            { 1, 1, 1, 0.248226956 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.100001
                                }
                                keyValues: list[f32] = {
                                    0
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
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9765625
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.39150941
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.100000001 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.13
                }
                emitterName: string = "GroundSplash"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_GroundSplash_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_GroundSplash_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.20000005 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    3.00471687
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
                                    0.5
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
                emitterName: string = "SplashEdge2"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, -6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    15.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, -6 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -78, -350, -1550 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                    }
                                    keyValues: list[f32] = {
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -78, -350, -1550 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.186522916
                            1
                        }
                        values: list[vec4] = {
                            { 0.701960802, 0.713725507, 0.78039217, 0 }
                            { 0.721568644, 0.768627465, 0.788235307, 0.407843143 }
                            { 0.968627453, 0.996078432, 1, 0 }
                        }
                    }
                }
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
                                    115
                                    -25
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
                    constantValue: vec3 = { 35, 35, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 35, 35, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
            }
        }
        visibilityRadius: f32 = 2500
        particleName: string = "TFT_Waterfall_Front_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Waterfall_Front_A"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Long" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Frog_Long"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Long"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_frog_long"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Fire"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_day_fire"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Wind_Constant_Night" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Wind_Constant_Night"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Wind_Constant_Night"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_air"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Koki" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Koki"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Koki"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_koki"
    }
    "Maps/Particles/TFT/Base/TFT_Water_WaterLily_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.00800000038
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 125
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_River_GrassRipple_03"
                        }
                    }
                }
                emitterName: string = "WaterPlane3"
                importance: u8 = 0
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.105263002
                            0.199445993
                            0.304708987
                            0.444597989
                            0.590027988
                            0.721607029
                            0.801939011
                            1
                        }
                        values: list[vec3] = {
                            { 3.55240798, 0, -5.68385267 }
                            { -3.35912919, 0, 5.37460661 }
                            { 3.03662157, 0, -4.85859442 }
                            { -2.43071365, 0, 3.88914204 }
                            { 6.019063, 0, -9.64509201 }
                            { -1.70861292, 0, 2.73378062 }
                            { 2.3145206, 0, -3.703233 }
                            { -1.19282651, 0, 1.90852237 }
                            { 0.0450607054, 0, -0.0720971301 }
                        }
                    }
                }
                shape: embed = VfxShape {
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
                                            1
                                            360
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00921699964
                            0.926267028
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
                pass: i16 = -7999
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.0700000003, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.0700000003, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 63, 63, 63 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterLily_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0199999996
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_River_GrassRipple_03"
                        }
                    }
                }
                emitterName: string = "WaterPlane4"
                importance: u8 = 0
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.108033001
                            0.196676001
                            0.331025004
                            0.444597989
                            0.598338008
                            0.721607029
                            0.825484991
                            1
                        }
                        values: list[vec3] = {
                            { 2.22320771, 0, -3.55713224 }
                            { -7.94402122, 0, 12.710434 }
                            { 5.02287912, 0, -8.03660679 }
                            { -4.77597141, 0, 7.64155436 }
                            { 3.90862656, 0, -6.26839304 }
                            { -4.03921556, 0, 6.46274519 }
                            { 5.02287912, 0, -8.03660679 }
                            { -3.22878456, 0, 5.1660552 }
                            { 0.0450607054, 0, -0.0720971301 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -20, 0, -143 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -100
                                        100
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 1 }
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
                                            1
                                            360
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0230410006
                            0.92396301
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
                pass: i16 = -7999
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.0700000003, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.0700000003, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterLily_01.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 150
        particleName: string = "TFT_Water_WaterLily_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_WaterLily_A"
    }
    "Maps/Particles/TFT/Base/TFT_Water_WaterLily_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.00800000038
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 125
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_River_GrassRipple_03"
                        }
                    }
                }
                emitterName: string = "WaterPlane3"
                importance: u8 = 0
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.105263002
                            0.199445993
                            0.304708987
                            0.444597989
                            0.590027988
                            0.721607029
                            0.801939011
                            1
                        }
                        values: list[vec3] = {
                            { 3.55240798, 0, -5.68385267 }
                            { -3.35912919, 0, 5.37460661 }
                            { 3.03662157, 0, -4.85859442 }
                            { -2.43071365, 0, 3.88914204 }
                            { 6.019063, 0, -9.64509201 }
                            { -1.70861292, 0, 2.73378062 }
                            { 2.3145206, 0, -3.703233 }
                            { -1.19282651, 0, 1.90852237 }
                            { 0.0450607054, 0, -0.0720971301 }
                        }
                    }
                }
                shape: embed = VfxShape {
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
                                            1
                                            360
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.784313798, 0.882353008, 0.882353008, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0161290001
                            0.880183995
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
                pass: i16 = -7999
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.0700000003, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.0700000003, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 45, 45 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterLily_01.dds"
                numFrames: u16 = 4
                startFrame: u16 = 2
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0199999996
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/SR/SRU_River_GrassRipple_03"
                        }
                    }
                }
                emitterName: string = "WaterPlane4"
                importance: u8 = 0
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.108033001
                            0.196676001
                            0.331025004
                            0.444597989
                            0.598338008
                            0.721607029
                            0.825484991
                            1
                        }
                        values: list[vec3] = {
                            { 2.22320771, 0, -3.55713224 }
                            { -7.94402122, 0, 12.710434 }
                            { 5.02287912, 0, -8.03660679 }
                            { -4.77597141, 0, 7.64155436 }
                            { 3.90862656, 0, -6.26839304 }
                            { -4.03921556, 0, 6.46274519 }
                            { 5.02287912, 0, -8.03660679 }
                            { -3.22878456, 0, 5.1660552 }
                            { 0.0450607054, 0, -0.0720971301 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -15, 0, -143 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -100
                                        100
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 1 }
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
                                            1
                                            360
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.792156935, 0.862745166, 0.882353008, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0783409998
                            0.921658993
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
                pass: i16 = -7999
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.0700000003, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.0700000003, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_WaterLily_01.dds"
                numFrames: u16 = 4
                startFrame: u16 = 3
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 150
        particleName: string = "TFT_Water_WaterLily_B"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Water_WaterLily_B"
    }
    "Maps/Particles/TFT/Base/TFT_Waterfall_Back_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Plane_B.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.150000006 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.550000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 10, 0, 0 }
                                { 30, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, -1.20000005 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls2"
                disabled: bool = true
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                pass: i16 = 20
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_02.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_02.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.400000006, -0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "TopEdgeHightlight"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_EdgeHiLite_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = 30
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                textureMult: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "SideFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_SideFoam_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.459998488 }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.699999988 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_Mult_01.NPE_MapsMountain.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.80000019
                }
                emitterName: string = "ShoreTop"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Shoretop_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00692840666
                            0.204291046
                            0.760950029
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.255319148 }
                            { 1, 1, 1, 0.380777866 }
                            { 1, 1, 1, 0.39579466 }
                            { 1, 1, 1, 0.248226956 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.100001
                                }
                                keyValues: list[f32] = {
                                    0
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
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9765625
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.39150941
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.100000001 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7.30000019
                }
                emitterName: string = "ShoreTopEdge"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_ShoreEdge_B.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.135040432
                            0.851482451
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.418439716 }
                            { 1, 1, 1, 0.78014183 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_ShoreTopEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.300000012 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_ShoreTopEdge_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.800000012 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.13
                }
                emitterName: string = "GroundSplash"
                disabled: bool = true
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_GroundSplash_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_GroundSplash_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.20000005 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "SplashEdge"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 230, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 230, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -120, 0 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -350, -170, -395 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -350, -170, -395 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
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
                                    100
                                    -75
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
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                }
                                keyValues: list[f32] = {
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
                            { 40, 40, 40 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SplashEdge_01.dds"
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SplashEdge_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.300000012, 0.400000006 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    3.00471687
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
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                emitterName: string = "SplashEdge2"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, -6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    15.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, -6 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 136, -140, -710 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                    }
                                    keyValues: list[f32] = {
                                        5.70754719
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 136, -140, -710 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.186522916
                            1
                        }
                        values: list[vec4] = {
                            { 0.701960802, 0.713725507, 0.78039217, 0 }
                            { 0.721568644, 0.768627465, 0.788235307, 0.407843143 }
                            { 0.968627453, 0.996078432, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
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
                                    115
                                    -25
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
                    constantValue: vec3 = { 35, 35, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 35, 35, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.4000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.4000001
                        }
                    }
                }
                emitterName: string = "SteamBot"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, -20 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -20, -2700, -390 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        5
                                        -6
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -20, -2700, -390 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
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
                                    115
                                    -25
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
                    constantValue: vec3 = { 53, 53, 53 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 53, 53, 53 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.100000001 }
                }
            }
        }
        visibilityRadius: f32 = 2500
        particleName: string = "TFT_Waterfall_Back_B"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Waterfall_Back_B"
    }
    "Maps/Particles/TFT/Base/TFT_Waterfall_Back_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Waterfall_Plane_A.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.150000006 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.550000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 10, 0, 0 }
                                { 30, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, -1.20000005 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                emitterName: string = "WhiteFalls2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Whitefalls_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_02.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_02.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.400000006, -0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "TopEdgeHightlight"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_EdgeHiLite_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = 30
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                textureMult: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "SideFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_SideFoam_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.459998488 }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.699999988 }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SideFoam_Mult_01.NPE_MapsMountain.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5.80000019
                }
                emitterName: string = "ShoreTop"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_Shoretop_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00692840666
                            0.204291046
                            0.760950029
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.255319148 }
                            { 1, 1, 1, 0.380777866 }
                            { 1, 1, 1, 0.39579466 }
                            { 1, 1, 1, 0.248226956 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.100001
                                }
                                keyValues: list[f32] = {
                                    0
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
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.9765625
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.39150941
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.100000001 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_TopFoam_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7.30000019
                }
                emitterName: string = "ShoreTopEdge"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_ShoreEdge_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.135040432
                            0.851482451
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.418439716 }
                            { 1, 1, 1, 0.78014183 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_ShoreTopEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.300000012 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_ShoreTopEdge_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -0.800000012 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.13
                }
                emitterName: string = "GroundSplash"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Waterfall_GroundSplash_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_GroundSplash_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.20000005 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "SplashEdge"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 230, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 230, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -120, 0 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -350, -170, -395 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.5
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -350, -170, -395 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
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
                                    100
                                    -75
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
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                }
                                keyValues: list[f32] = {
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
                            { 40, 40, 40 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SplashEdge_01.dds"
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_SplashEdge_Mult_01.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.300000012, 0.400000006 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    3.00471687
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
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                emitterName: string = "SplashEdge2"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, -6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    15.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, -6 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -49, -180, -399 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                    }
                                    keyValues: list[f32] = {
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -49, -180, -399 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.186522916
                            1
                        }
                        values: list[vec4] = {
                            { 0.701960802, 0.713725507, 0.78039217, 0 }
                            { 0.721568644, 0.768627465, 0.788235307, 0.407843143 }
                            { 0.968627453, 0.996078432, 1, 0 }
                        }
                    }
                }
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
                                    115
                                    -25
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
                    constantValue: vec3 = { 35, 35, 35 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 35, 35, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.4000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.4000001
                        }
                    }
                }
                emitterName: string = "SteamBot"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, -20 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -20, -2700, -390 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        5
                                        -6
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -20, -2700, -390 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
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
                                    115
                                    -25
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
                    constantValue: vec3 = { 53, 53, 53 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 53, 53, 53 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.NPE_MapsMountain.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
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
                textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.NPE_MapsMountain.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.100000001 }
                }
            }
        }
        visibilityRadius: f32 = 2500
        particleName: string = "TFT_Waterfall_Back_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Waterfall_Back_A"
    }
    "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Crickets" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Crickets"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Crickets"
        soundPersistentDefault: string = "Play_sfx_tft_env_base_night_cricket"
    }
    "Maps/Particles/TFT/TFT_Skybox" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "TFT_Skybox_Bot"
                disabled: bool = true
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Particles/TFT_Default_Skybox1.scb"
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                texture: string = "ASSETS/Particles/TFT_Default_Skybox1.dds"
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
                emitterName: string = "TFT_Skybox_Walls"
                disabled: bool = true
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Particles/TFT_Default_Skybox2.scb"
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                texture: string = "ASSETS/Particles/TFT_Default_Skybox2.dds"
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
                emitterName: string = "Clouds_A"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0199999996, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
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
                emitterName: string = "Clouds_B"
                importance: u8 = 2
                translationOverride: vec3 = { 1, -1, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_B.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Cloud_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
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
                scaleOverride: vec3 = { 16, 16, 16 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.00499999989
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
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
                            -1
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "Wind"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -450, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Wind.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.90196079, 0.788235307, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.603921592, 0.254901975, 1 }
                }
                pass: i16 = -9999
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Env_TFT_Skybox_Wind.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
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
                            { 0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
                            { 0, 0 }
                        }
                    }
                }
                uvTransformCenter: vec2 = { 1, 1 }
                scaleOverride: vec3 = { 17.5, 17.5, 17.5 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.129999995
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Clouds_A_Thunder"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -550, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
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
                                    1
                                }
                            }
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
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
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
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0524475537
                            0.0909090936
                            0.141608387
                            0.279720277
                            0.307692319
                            0.442307681
                            0.472027957
                            0.604895115
                            0.674825191
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.0233015642 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.294182241 }
                            { 1, 1, 1, 0.0145634776 }
                            { 1, 1, 1, 0.154372856 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.14563477 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9999
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0199999996, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.20000005, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
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
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 3
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.129999995
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Clouds_B_Thunder"
                importance: u8 = 2
                translationOverride: vec3 = { 1, -1, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_B.scb"
                    }
                }
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
                                    1
                                }
                            }
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
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
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
                            0.00349650346
                            0.0506993011
                            0.113636367
                            0.157342657
                            0.279720277
                            0.307692319
                            0.433566421
                            0.604895115
                            0.627622366
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.378640771 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.621359229 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.980582535 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.281553388 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9996
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
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
                scaleOverride: vec3 = { 16, 16, 16 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                            1.5
                        }
                    }
                }
                emitterName: string = "TFT_Skybox_WallsL"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -65, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Whole.scb"
                    }
                }
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
                                    1
                                }
                            }
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
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
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
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0524475537
                            0.0909090936
                            0.141608387
                            0.279720277
                            0.307692319
                            0.442307681
                            0.472027957
                            0.604895115
                            0.674825191
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.0233015642 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.294182241 }
                            { 1, 1, 1, 0.0145634776 }
                            { 1, 1, 1, 0.154372856 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.14563477 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9998
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Default_Skybox2_Mask.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
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
                emitterName: string = "Clouds_A1"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -450, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.827450991, 0.894117653, 1 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00300000003, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox"
        particlePath: string = "Maps/Particles/TFT/TFT_Skybox"
        flags: u8 = 197
    }
    "Maps/Particles/SR/SRU_River_GrassRipple_03" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                emitterName: string = "WaterPlane1"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/SRU_river_grassripple_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.643106997 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_River_GrassRipple_01.NPE_MapsMountain.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.300000012 }
                }
            }
        }
        visibilityRadius: f32 = 150
        particleName: string = "SRU_River_GrassRipple_03"
        particlePath: string = "Maps/Particles/SR/SRU_River_GrassRipple_03"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Lighting_Rift_Alternate" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x64857365 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1913.31372, 448.613586, 890.376465, 1
                }
                name: string = "Light_ShadowFill_02_2"
            }
            0x99c95b3e = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    799.127625, 473.429565, 2511.76514, 1
                }
                name: string = "Light_ShadowFill_01_1"
            }
            0x61d7394a = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    328.176941, 447.464417, 2980.6831, 1
                }
                name: string = "Light_ShadowFill_01_2"
            }
            0x04c8d0d2 = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1224.45483, 632.808472, 3655.14844, 1
                }
                name: string = "Light_ShadowFill_01_3"
            }
            0x5a8f2d8a = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1339.13855, 470.766907, 3085.09253, 1
                }
                name: string = "Light_ShadowFill_01_4"
            }
            0xde292132 = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3004.97412, 468.862488, 3127.11987, 1
                }
                name: string = "Light_ShadowFill_01_5"
            }
            0xca2bbdd6 = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3401.77881, 263.22998, 1545.53052, 1
                }
                name: string = "Light_ShadowFill_01_6"
            }
            0x647d71df = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    628.123474, 245.054962, 1037.41455, 1
                }
                name: string = "Light_ShadowFill_01_7"
            }
            0xe2723afc = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3454.02417, 119.74231, 940.953491, 1
                }
                name: string = "Light_ShadowFill_01_8"
            }
            0x2adf745d = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    819.268188, 327.986237, 1724.32837, 1
                }
                name: string = "Light_ShadowFill_01_9"
            }
            0xd9056f6d = MapPointLight {
                type: link = 0xe0aaf3ff
                radiusScale: f32 = 1.54788196
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2179.39771, 372.52179, 2005.93091, 1
                }
                name: string = "Light_ShadowFill_01_10"
            }
            0x80332d00 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.10465991
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1817.73621, 508.198669, 1982.14075, 1
                }
                name: string = "Light_ShadowFill_02_1"
            }
            0x3b01a2a1 = MapPointLight {
                type: link = 0xcf3f62c2
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1039.8761, 244.635681, 997.016968, 1
                }
                name: string = "Light_Torch_01_1"
            }
            0x4fb96515 = MapPointLight {
                type: link = 0xcf3f62c2
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2885.20679, 244.635681, 997.016968, 1
                }
                name: string = "Light_Torch_01_2"
            }
            0xea6e004c = MapPointLight {
                type: link = 0xcf3f62c2
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1123.55383, 244.635681, 3051.27759, 1
                }
                name: string = "Light_Torch_01_3"
            }
            0xe96056fc = MapPointLight {
                type: link = 0xcf3f62c2
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2967.51074, 244.635681, 3051.27759, 1
                }
                name: string = "Light_Torch_01_4"
            }
            0xcc4a3d85 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3283.09424, 448.613708, 1238.59228, 1
                }
                name: string = "Light_ShadowFill_02_3"
            }
            0x33cacc8a = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3609.26978, 594.876648, 3277.59546, 1
                }
                name: string = "Light_ShadowFill_02_4"
            }
            0x66387984 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    767.869385, 594.87616, 3140.36963, 1
                }
                name: string = "Light_ShadowFill_02_5"
            }
            0x007f0030 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    176.96106, -160.753769, 1740.91321, 1
                }
                name: string = "Light_ShadowFill_02_6"
            }
            0x1492207a = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3653.14404, -160.753281, 2131.91113, 1
                }
                name: string = "Light_ShadowFill_02_7"
            }
            0x9c11c104 = MapLightingVolume {
                sunColor: vec4 = { 0.270588249, 0.411764711, 0.643137276, 1 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.200000003 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.447058827, 0.388235301, 0.533333361, 1 }
                horizonColor: vec4 = { 0.525490224, 0.643137276, 0.815686285, 1 }
                groundColor: vec4 = { 0.34117648, 0.160784319, 0.223529413, 1 }
                skyLightScale: f32 = 0.800000012
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.247058824, 0.23137255, 0.490196079, 1 }
                fogAlternateColor: vec4 = { 0.176470593, 0.168627456, 0.250980407, 1 }
                fogStartAndEnd: vec2 = { 800, -1800 }
                transform: mtx44 = {
                    2300, 0, 0, 0
                    0, 3500, 0, 0
                    0, 0, 2500, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume1"
            }
            0x3397ab33 = MapPointLight {
                type: link = 0xe1aaf592
                radiusScale: f32 = 1.27488661
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1913.31372, 448.613586, 2898.5144, 1
                }
                name: string = "Light_ShadowFill_02_8"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Lighting_Rift_Alternate"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Audio_Base_Night" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xba32c134 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Pond_Night"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1982.99402, 174.274658, 861.556519, 1
                }
                name: string = "TFT_Audio-Emitter_Pond1"
            }
            0x41fe632f = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Waterfall"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3464.76587, 210.955322, 2534.6001, 1
                }
                name: string = "TFT_Audio-Emitter_Waterfall1"
            }
            0x782d562d = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Waterfall"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    634.694946, 14.1040039, 2250.86523, 1
                }
                name: string = "TFT_Audio-Emitter_Waterfall2"
            }
            0xe5d2e8cc = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1036.2627, 207.78302, 996.088623, 1
                }
                name: string = "TFT_Audio-Emitter_Fire1"
            }
            0x6647b230 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2886.45776, 207.783005, 994.656982, 1
                }
                name: string = "TFT_Audio-Emitter_Fire2"
            }
            0xd7c41ddb = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1124.64771, 207.783005, 3052.84595, 1
                }
                name: string = "TFT_Audio-Emitter_Fire3"
            }
            0x2a7001a5 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2965.7561, 207.783005, 3052.66894, 1
                }
                name: string = "TFT_Audio-Emitter_Fire4"
            }
            0x7443a481 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Koki"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1594.6759, 243.296021, 2075.32202, 1
                }
                name: string = "TFT_Audio-Emitter_Birds1"
            }
            0x6d9bba2b = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Crickets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2950.97021, 492.708618, 1981.32666, 1
                }
                name: string = "TFT_Audio-Emitter_Birds_Dove_Oneshots1"
            }
            0xad328051 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Wind_Constant_Night"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1890.67126, 271.898682, 1423.62549, 1
                }
                name: string = "TFT_Audio-Emitter_Wind_Constant1"
            }
            0x8e288198 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Long"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    852.717407, 13.6604004, 1756.16333, 1
                }
                name: string = "TFT_Audio-Emitter_Frog_Long1"
            }
            0xcb44daf1 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Short"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3270.42163, -5.23461914, 2057.86084, 1
                }
                name: string = "TFT_Audio-Emitter_Frog_Short1"
            }
            0x6291637c = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Pond_Night"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2171.33472, -8.37402344, 4343.77441, 1
                }
                name: string = "TFT_Audio-Emitter_Pond_Night1"
            }
            0x0b43c4ec = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Frog_Short"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    416.135254, 13.8161621, 3183.09131, 1
                }
                name: string = "TFT_Audio-Emitter_Frog_Short2"
            }
            0xb6e4736b = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Crickets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    781.865234, 176.445557, 1912.17297, 1
                }
                name: string = "TFT_Audio-Emitter_Crickets1"
            }
            0x9af1c170 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Audio-Emitter_Crickets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    940.289917, 100.918274, 2309.67529, 1
                }
                name: string = "TFT_Audio-Emitter_Crickets2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Audio_Base_Night"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2915.95557, 11.2485962, 2462.1416, 1
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
                    1103.59802, 11.2485962, 1615.37769, 1
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
                    2801, 0, 2911.16626, 1
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
                    1203.64636, 0, 1140.53381, 1
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
                    2957.82544, 0, 2927.14917, 1
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
                    1042.78552, 0, 1122.86438, 1
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
                    1421.01526, 0, 1458, 1
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
                    1187.76733, 0, 1388.43628, 1
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
                    2832.14062, 0, 2664.4563, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Design_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Skybox_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdf91013f = null
            0xb7d10038 = MapParticle {
                system: link = "Maps/Particles/TFT/TFT_Skybox"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 18.6372032, 2000, 1
                }
                name: string = "TFT_Skybox1"
                0xccf79327: u8 = 62
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Skybox_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xb0b6623a = null
            0x4b242f17 = null
            0x4f3db772 = null
            0x654262b5 = null
            0xef149bf0 = null
            0xe66e0221 = null
            0x530db2a7 = null
            0x96910f98 = null
            0xe19b3d91 = null
            0xe8b897af = null
            0x33ed62ea = null
            0x9e54ced2 = null
            0x04d5c5db = null
            0x4be86d70 = null
            0x013d9018 = null
            0x7aaefc50 = null
            0x1e6738f7 = null
            0xe7e8d246 = null
            0xc1833276 = null
            0x66057b1f = null
            0x27e3894b = null
            0x46b485de = null
            0xb4f3b9e9 = null
            0xf85f77e3 = null
            0x75cf2bf0 = null
            0x47770491 = null
            0xdea6e963 = null
            0x1d19e82f = null
            0x17f50e8f = null
            0x317a6a1b = null
            0x1797ee7f = null
            0x123ff364 = null
            0x5e41e5d4 = null
            0x7052d6da = null
            0x883b0a18 = null
            0xc03400ce = null
            0x10a6627f = null
            0x3fb7abfa = null
            0xa3414a2c = null
            0x500f6173 = null
            0xa94f780d = null
            0x94989302 = null
            0xa49f46d0 = null
            0x64fd72be = null
            0x7c25c963 = null
            0x47db92da = null
            0xd1d98496 = null
            0xcfa61aaf = null
            0x5c91c1c9 = null
            0xe8585849 = null
            0x584e7a5e = null
            0x6c73a3bb = null
            0xbdadd77f = null
            0x732a4d31 = null
            0x21e72ff0 = null
            0xdec289ba = null
            0x4dd815f5 = null
            0x3a83108f = null
            0xce8db334 = null
            0xe4f1ff37 = null
            0x955669ab = null
            0x4408c009 = null
            0x65d30be5 = null
            0x4c707a65 = null
            0x446f96cf = null
            0xdc66f4d7 = null
            0x3ed5aab2 = null
            0x8154c573 = null
            0xab285a01 = null
            0x178223b0 = null
            0xd8dec41c = null
            0x1ca7f2ea = null
            0x2428c507 = null
            0xb006410a = null
            0xdeb4c24b = null
            0x20e693f4 = null
            0x9053d43c = null
            0x5488f625 = null
            0xf112771c = null
            0xc221f436 = null
            0xb7887711 = null
            0xef8cb769 = null
            0xc41087fa = null
            0xe0e4c74d = null
            0x799a6222 = null
            0xcb8654e0 = null
            0x766c223c = null
            0x5b56df58 = null
            0xf873ac30 = null
            0x86d5d1b1 = null
            0x47007661 = null
            0xaef51dec = null
            0xfa345fc2 = null
            0x9c653c70 = null
            0x1128a289 = null
            0x38a463c3 = null
            0x237f60ab = null
            0x7b09de13 = null
            0x577e0473 = null
            0x32c3fb48 = null
            0xb5c5dd5b = null
            0x1241793b = null
            0x73a462aa = null
            0xbb281898 = null
            0x4f06fdd6 = null
            0x4c8e652b = null
            0x621b7332 = null
            0xede575f6 = null
            0xb730fcdf = null
            0x35764bd1 = null
            0xdf0ef377 = null
            0x0cb1300d = null
            0xa643b637 = null
            0x2645dfc7 = null
            0x5078cb6c = null
            0x43bc3179 = null
            0xb4641941 = null
            0xe7cc1f62 = null
            0x613ad5a1 = null
            0xb6368c4b = null
            0xc91f74c6 = null
            0x7d70cacb = null
            0x90b54822 = null
            0xeb79aced = null
            0xf33d7533 = null
            0x05d0eb6f = null
            0x4736388a = null
            0xa19aa8f4 = null
            0xc5da5ecf = null
            0xd45bd79b = null
            0x4ea220bd = null
            0xcfc2205b = null
            0x8975c0cb = null
            0xffeba0b7 = null
            0x0b1b7eaa = null
            0x39a50f61 = null
            0x24e00cc4 = null
            0x8047e246 = null
            0x6187ec0e = null
            0xab2acccb = null
            0x5d8884be = null
            0x78f29f92 = null
            0x8b014a8a = null
            0x52e3c2d5 = null
            0xe9728805 = null
            0xae7aef55 = null
            0x3c8de35a = null
            0x8a77465a = null
            0x9f59c603 = null
            0x4aa6f7e8 = null
            0xffaa08eb = null
            0x8e839db5 = null
            0xcc229aeb = null
            0xb58a5c74 = null
            0x47696b46 = null
            0xd6dcacd8 = null
            0x54b32da3 = null
            0xf774ad2a = null
            0x858f8199 = null
            0xa232c4f9 = null
            0x01a644cf = null
            0xf25b52b8 = null
            0x23935aed = null
            0x0fd7f239 = null
            0x633a12a5 = null
            0x49851f6f = null
            0xf6417974 = null
            0x3b7547f2 = null
            0x112da919 = null
            0x19c7aad5 = null
            0x6951b06e = null
            0xef2a5c8f = null
            0xe6f01af9 = null
            0x53cd64df = null
            0x45db22cb = null
            0xefd04ec4 = null
            0x808da3c5 = null
            0xb0b6e3f7 = null
            0x8b62b3d8 = null
            0xc42fbfb8 = null
            0xcf569d95 = null
            0x495f4059 = null
            0x2dfa5108 = null
            0x76b8e583 = null
            0x9a8905e6 = null
            0x83b48b12 = null
            0xc745c4fe = null
            0x98551ce7 = null
            0x31fa41a7 = null
            0xd64e6269 = null
            0x9a37203f = null
            0x909c13b2 = null
            0xc31bb059 = null
            0xdcc57c7c = null
            0x8fc01448 = null
            0x4cfda4f0 = null
            0x3d570734 = null
            0xc0646aa6 = null
            0xd1eb659a = null
            0x6e5f1fb7 = null
            0x1b4d1522 = null
            0x92b2482c = null
            0xcb1acf84 = null
            0x5e4a5757 = null
            0x2a1050d6 = null
            0x87979425 = null
            0x9d7560ab = null
            0xaf898c55 = null
            0x179616e0 = null
            0xc0676999 = null
            0xadaeee1e = null
            0xe0660b17 = null
            0x687f4be3 = null
            0x8f72bd21 = null
            0x6cef439c = null
            0x28e78528 = null
            0x02a695d0 = null
            0x233e4d02 = null
            0x1a615461 = null
            0xb4d100b9 = null
            0xefcdc3ce = null
            0x38dad135 = null
            0xeb513072 = null
            0xeb8ff5ad = null
            0xbef8ced7 = null
            0x676ec377 = null
            0x6c4ac3c1 = null
            0x21692b75 = null
            0x1f67071b = null
            0x5b9bf726 = null
            0x949fa27e = null
            0xd07fe682 = null
            0x00909c50 = null
            0x854643d8 = null
            0x8a26752d = null
            0x9d7c2638 = null
            0x23584c47 = null
            0x672726d4 = null
            0x16da303a = null
            0x53c9f8b6 = null
            0x72d5afff = null
            0x84fb3863 = null
            0x4139561e = null
            0x529a4cad = null
            0x87b5cb3d = null
            0xe47831eb = null
            0x3bcc9da0 = null
            0x8b9c9cef = null
            0xa8135e1c = null
            0xb3de144f = null
            0xae494806 = null
            0x0a78b7f4 = null
            0x83a33f52 = null
            0xf52f101b = null
            0x52053708 = null
            0x93b23bc8 = null
            0xebe7512d = null
            0x2a707da4 = null
            0x3a694c4f = null
            0x9f84ce83 = null
            0xf2c68eef = null
            0x8e171705 = null
            0xb35e5163 = null
            0x7ebc2ae1 = null
            0x2e7bf13d = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/VFX_Rift_Alternate" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2a2d85b4 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1121.42773, 163.975723, 3053.40723, 1
                }
                name: string = "TFT_BrazierFire_B1"
            }
            0x7f845930 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2965.1748, 163.975723, 3053.40723, 1
                }
                name: string = "TFT_BrazierFire_B2"
            }
            0xd9fd2435 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1038.75769, 163.975739, 991.348022, 1
                }
                name: string = "TFT_BrazierFire_B3"
            }
            0x5006ad0b = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_Rift_Alternate"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2886.37109, 163.975739, 991.348022, 1
                }
                name: string = "TFT_BrazierFire_B4"
            }
            0x6ebc9b8c = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1211.6958, 143.204285, 3470.39966, 1
                }
                name: string = "TFT_Map_Fireflies1"
            }
            0x07b0bd2c = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    258.44046, 103.393311, 2780.58496, 1
                }
                name: string = "TFT_Map_Fireflies2"
            }
            0x550ce32c = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    730.372009, 81.4441299, 1463.09363, 1
                }
                name: string = "TFT_Map_Fireflies3"
            }
            0x0c68affb = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3411.23828, -70.9773865, 1492.86011, 1
                }
                name: string = "TFT_Map_Fireflies4"
            }
            0xddcee795 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3269.31982, 76.1120605, 2724.3186, 1
                }
                name: string = "TFT_Map_Fireflies5"
            }
            0xb4ce3605 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Map_Fireflies_Dark"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1322.65552, 129.235687, 832.117615, 1
                }
                name: string = "TFT_Map_Fireflies6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/VFX_Rift_Alternate"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Art_Rift_Alternate" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x364df54a = null
            0x9b767d91 = null
            0xedcd5a90 = null
            0x69a01cf9 = null
            0x00462071 = null
            0xa4bd4b6a = null
            0x462cebff = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Sparks_Blue"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1993.09253, -1069.81812, 1987.78589, 1
                }
                name: string = "TFT_Sparks_Blue1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Art_Rift_Alternate"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/VFX_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x3dc1d605 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Waterfall_Back_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    665.345093, -38.6470795, 2894.89722, 1
                }
                name: string = "TFT_Waterfall_Back_A1"
            }
            0xaa052b55 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/Waterfall_Edge_Ripple_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1899.02551, -92.2881775, 878.272339, 1
                }
                name: string = "Waterfall_Edge_Ripple_A1"
            }
            0xaec6526a = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Waterfall_Back_B"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2867.37085, -34.5657196, 3297.56445, 1
                }
                name: string = "TFT_Waterfall_Back_B1"
            }
            0x84074316 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_Ripple_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2082.59033, -34.2425079, 3171.53857, 1
                }
                name: string = "TFT_Water_Ripple_A1"
            }
            0xa854433e = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_RippleWavy_A"
                transform: mtx44 = {
                    0.0332028866, 0, -0.999448717, 0
                    0, 1, 0, 0
                    0.999448717, 0, 0.0332028866, 0
                    1478.89612, -59.4942322, 849.927429, 1
                }
                name: string = "TFT_Water_RippleWavy_A1"
            }
            0xab18b2c2 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_RippleWavy_A"
                transform: mtx44 = {
                    0.942878604, 0, -0.333136648, 0
                    0, 1, 0, 0
                    0.333136648, 0, 0.942878604, 0
                    3473.67285, -53.5256958, 2995.67065, 1
                }
                name: string = "TFT_Water_RippleWavy_A2"
            }
            0xcef82a30 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_RippleWavy_A"
                transform: mtx44 = {
                    0.994058251, 0, 0.108849555, 0
                    0, 1, 0, 0
                    -0.108849555, 0, 0.994058251, 0
                    2747.42261, -72.4771652, 827.127625, 1
                }
                name: string = "TFT_Water_RippleWavy_A3"
            }
            0x83cd366a = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_WaterLily_A"
                transform: mtx44 = {
                    0.210626066, 0, -0.977566719, 0
                    0, 1, 0, 0
                    0.977566719, 0, 0.210626066, 0
                    1394.70483, -47.4658203, 872.57843, 1
                }
                name: string = "TFT_Water_WaterLily_A1"
            }
            0x294406c9 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_WaterLily_B"
                transform: mtx44 = {
                    0.64218533, 0, -0.766549408, 0
                    0, 1, 0, 0
                    0.766549408, 0, 0.64218533, 0
                    2189.5769, -46.4886017, 945.473938, 1
                }
                name: string = "TFT_Water_WaterLily_B1"
            }
            0xb42ffcd7 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_WaterLily_B"
                transform: mtx44 = {
                    0.153653502, 0, 0.988125086, 0
                    0, 1, 0, 0
                    -0.988125086, 0, 0.153653502, 0
                    2486.91528, -46.4888153, 871.288269, 1
                }
                name: string = "TFT_Water_WaterLily_B2"
            }
            0x0278eeae = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_A"
                transform: mtx44 = {
                    0.708549023, 0, -0.705661595, 0
                    0, 1, 0, 0
                    0.705661595, 0, 0.708549023, 0
                    1537.58569, -59.8084259, 935.981812, 1
                }
                name: string = "TFT_Water_WaterCaustics_A1"
            }
            0xd90f6682 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_WaterCaustics_B"
                transform: mtx44 = {
                    0.999023855, 0, 0.0441741236, 0
                    0, 1, 0, 0
                    -0.0441741236, 0, 0.999023855, 0
                    2271.83081, -58.1734772, 923.671387, 1
                }
                name: string = "TFT_Water_WaterCaustics_B1"
            }
            0x0ebc73d9 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Waterfall_Front_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, -0, 2000, 1
                }
                name: string = "TFT_Waterfall_Front_A1"
            }
            0xeabcbf65 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Waterfall_Front_B"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 15, 2000, 1
                }
                name: string = "TFT_Waterfall_Front_B1"
            }
            0xd8508e87 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_Water_Ripple_B"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2002.09717, 4.05621338, 1996.50537, 1
                }
                name: string = "TFT_Water_Ripple_B1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/VFX_Shared"
    }
    "Maps/MapGeometry/Map22/Base_Rift_Alternate" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Base_Rift_Alternate"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.549019635, 0.505882382, 0.431372553, 1 }
                sunDirection: vec3 = { -0.384805739, 0.827142715, -0.409584463 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.282352954, 0.203921571, 0.113725491, 1 }
                horizonColor: vec4 = { 0.411764711, 0.321568638, 0.227450982, 1 }
                groundColor: vec4 = { 0.368627459, 0.392156869, 0.360784322, 1 }
                skyLightScale: f32 = 1.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -500, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 0.850000024
                lightGridCharacterFullBrightIntensity: f32 = 0.400000006
                0x2f3b5471: f32 = 3
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Base_Rift_Alternate/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.75
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Base_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            "Art_Shared" = "Maps/MapGeometry/Map22/Chunks/Base/Art_Shared"
            "VFX_Shared" = "Maps/MapGeometry/Map22/Chunks/Base/VFX_Shared"
            "Design_Base" = "Maps/MapGeometry/Map22/Chunks/Base/Design_Base"
            "Audio_Base_Night" = "Maps/MapGeometry/Map22/Chunks/Base/Audio_Base_Night"
            "Lighting_Rift_Alternate" = "Maps/MapGeometry/Map22/Chunks/Base/Lighting_Rift_Alternate"
            "VFX_Rift_Alternate" = "Maps/MapGeometry/Map22/Chunks/Base/VFX_Rift_Alternate"
            "Art_Rift_Alternate" = "Maps/MapGeometry/Map22/Chunks/Base/Art_Rift_Alternate"
            "Skybox_Base" = "Maps/MapGeometry/Map22/Chunks/Base/Skybox_Base"
        }
    }
    0xcf3f62c2 = MapPointLightType {
        lightColor: vec4 = { 0.450980395, 1, 0.984313726, 1 }
        radius: f32 = 550
        specular: bool = false
    }
    0xe0aaf3ff = MapPointLightType {
        lightColor: vec4 = { 0.223529413, 0.466666669, 0.749019623, 1 }
        radius: f32 = 600
        Impact: i32 = 1
    }
    0xe1aaf592 = MapPointLightType {
        lightColor: vec4 = { 0.235294119, 0.247058824, 0.870588243, 1 }
        radius: f32 = 1000
        castStaticShadows: bool = false
        specular: bool = false
        Impact: i32 = 1
    }
}
