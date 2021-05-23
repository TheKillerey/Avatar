#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_middle_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Floaty_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 50, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bobbing_Rate"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Secondary_Rotation_Rate"
                value: vec4 = { 0.138999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Primary"
                value: vec4 = { 0.5, 0, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Primary"
                value: vec4 = { -0.0199999996, 0.0199999996, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Secondary"
                value: vec4 = { -0.0799999982, 0.0799999982, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Secondary"
                value: vec4 = { 0.699999988, 1, -0.300000012, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Translate_Axis"
                value: vec4 = { 0, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_RANDOM_SECONDARY_MOTION"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_FloatingObjects"
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Bench_Slab_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Flat_Top_C.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Blackhole_Rock_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Tall_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Models/Spaceship_Engine_Lights_A/Materials/ENV_SimpleRotate_Engine_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Spaceship_Engine_Lights_A/Materials/ENV_SimpleRotate_Engine_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Spaceship_Engine_Lights_A.TFT_ArenaSkin_Galaxy2.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Axis"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { 0.0399999991, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ColorDodge_Amount"
                value: vec4 = { 0.100000001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0.349999994, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_SimpleRotate"
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Spaceship_Engine_A/Materials/Spaceship_Emissive_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Spaceship_Engine_A/Materials/Spaceship_Emissive_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { 0, 0.678431392, 0.643137276, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Battery_MAT_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Battery_MAT_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Spaceship_Battery_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_Spaceship_MAT_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_Spaceship_MAT_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Spaceship_Bench_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Trim_Metal_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Trim_Metal_A_inst"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Tile_Metal_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Tile_Metal_A_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Metal_Tileable_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Stripes_A.TFT_ArenaSkin_Odyssey_Polish.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Engine_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Spaceship_Engine_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Spaceship_Engine_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/ENV_TileableDiffuse_Hangar_Tile_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/ENV_TileableDiffuse_Hangar_Tile_inst"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_MAT_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Bench_MAT_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Bench_A.TFT_ArenaSkin_Odyssey_Polish.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_Spaceship_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_Spaceship_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Board_Spaceship_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Goldmine_Base_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_Spaceship" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa50b9317 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1912.65027, 39.7043457, 2046.26562, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop1"
            }
            0xfe0fd1d1 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Thrusters"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    884.148926, 247.897217, 3033.37109, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Spaceship_Thrusters1"
            }
            0x6182d21b = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Amb"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1883.94824, -0.000244140625, 2230.89575, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Spaceship_Amb1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_Spaceship"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Spaceship" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x86c14eb6 = MapLightingVolume {
                sunColor: vec4 = { 0.596078455, 0.486274511, 0.486274511, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                0xba02f116: f32 = 0.100000001
                skyLightColor: vec4 = { 0.427450985, 0.56078434, 0.607843161, 1 }
                horizonColor: vec4 = { 0.392156869, 0.431372553, 0.627451003, 1 }
                groundColor: vec4 = { 0.23137255, 0.235294119, 0.372549027, 1 }
                skyLightScale: f32 = 0.5
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.184313729, 0.145098045, 0.298039228, 1 }
                fogAlternateColor: vec4 = { 0.360784322, 0.184313729, 0.388235301, 1 }
                fogStartAndEnd: vec2 = { 250, -750 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2186.59424, -927.355957, 2144.35596, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Spaceship"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Spaceship" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x298bf786 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Wind"
                colorModulate: vec4 = { 1, 1, 1, 0.459998488 }
                transform: mtx44 = {
                    -0.953529, 0, -0.301304162, 0
                    0, 1, 0, 0
                    0.301304162, 0, -0.953529, 0
                    1826.55151, 158.593597, 1699.44568, 1
                }
                name: string = "Galaxy_Blackhole_Wind3"
            }
            0x906a6be4 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Wind"
                colorModulate: vec4 = { 1, 1, 1, 0.500007629 }
                transform: mtx44 = {
                    -0.978626251, 0, -0.205649421, 0
                    0, 1, 0, 0
                    0.205649421, 0, -0.978626251, 0
                    2502.6394, 158.593475, 2424.47925, 1
                }
                name: string = "Galaxy_Blackhole_Wind4"
            }
            0x7a6c626f = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -8.74227766e-08, 0, 0.99999994, 0
                    -0.207382411, 0.978259921, -1.81299473e-08, 0
                    -0.978259861, -0.207382426, -8.55221955e-08, 0
                    748.652039, 152.178299, 1335.31982, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens9"
            }
            0x51f9c888 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 0.96677357, 0.255634427, 0
                    0, -0.255634427, 0.96677357, 0
                    883.442444, 153.765396, 1460.43225, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens7"
            }
            0x2b319ed0 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -0.0190183297, -0.00454938551, 0.649705708, 0
                    -0.209489122, 0.772084057, -0.000725904538, 0
                    -0.964661777, -0.261769444, -0.0300707631, 0
                    742.202454, 143.953201, 1195.74304, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens8"
            }
            0x91ed0ba5 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Arena_JetThruster01"
                transform: mtx44 = {
                    -0.0180725418, 0.29813996, 1.97757077, 0
                    -0.749969304, -0.00100510684, -0.00670225825, 0
                    -1.40443444e-05, -1.97765136, 0.29815203, 0
                    307.075317, -406.278473, 1896.65417, 1
                }
                name: string = "TFT_Odyssey_Jinx_Arena_JetThruster01_1"
                0xccf79327: u8 = 126
            }
            0xd17233fc = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Arena_JetThruster01"
                transform: mtx44 = {
                    -0.0158789363, 0.192257434, 1.9906745, 0
                    -0.749969304, 0.00265246769, -0.00623842515, 0
                    -0.00863942876, -1.99072492, 0.192193419, 0
                    342.840515, -412.629394, 2758.71655, 1
                }
                name: string = "TFT_Odyssey_Jinx_Arena_JetThruster01_2"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Spaceship"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2942.92432, 11.2485962, 2437.69849, 1
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
                    1067.23218, 11.2485962, 1695.15454, 1
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
                    1187.73376, 0, 1111.19238, 1
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
                    3021.10547, 0, 2859.89062, 1
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
                    856.235291, 0, 1091.79797, 1
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
                    1102.27698, 0, 1388.43628, 1
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
                    2857.91894, 0, 2664.4563, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xba8e619d = null
            0x14f24b35 = null
            0xcb9ea52b = null
            0xbfd6d17b = null
            0xd85318ca = null
            0x36ab4d65 = null
            0x064c2ec7 = null
            0xdd04ff6d = null
            0x89a340f2 = null
            0x8f3da9dc = null
            0x21bce7df = null
            0x2b49cf67 = null
            0xd520d00a = null
            0xec5d5e1f = null
            0x749e5085 = null
            0x00340dfb = null
            0xbb2a9779 = null
            0xd5c3a729 = null
            0xde1438c4 = null
            0xd6c11eaa = null
            0x7876eddd = null
            0x39d57c0f = null
            0xded04944 = null
            0xb5da60a1 = null
            0x45e0b849 = null
            0x65dec31c = null
            0x52568464 = null
            0xd0acb03f = null
            0x1865d60b = null
            0x33c158c4 = null
            0x73f1d490 = null
            0x2b1c28c0 = null
            0xa6fa1fad = null
            0x00217c05 = null
            0x0023f348 = null
            0x3ae68076 = null
            0xd6f09b51 = null
            0x793a2d79 = null
            0x769fdd22 = null
            0xd851e914 = null
            0x52d65aa3 = null
            0x6305ec15 = null
            0x5533c5e4 = null
            0x7de801ee = null
            0x0d683e83 = null
            0xd09c65cb = null
            0x3ac49e11 = null
            0x60596833 = null
            0xec0ef9cb = null
            0x08353a55 = null
            0xf52848f4 = null
            0x0329ab2a = null
            0xa8d22761 = null
            0xfe12b7f3 = null
            0x8e7f8320 = null
            0x41fe3344 = null
            0xd0f4914c = null
            0x3dd75f9d = null
            0x12a8a342 = null
            0x862ff418 = null
            0x9bba1c71 = null
            0x2336fb15 = null
            0xa70f0665 = null
            0xb583a22f = null
            0x4dabf34d = null
            0xcdbcc208 = null
            0xb7be64dc = null
            0x015c895d = null
            0xb6e0109c = null
            0x0c5e9ccc = null
            0xf6d562bb = null
            0xb0c179ba = null
            0xc3eebfb1 = null
            0xa06d19b5 = null
            0x9b1d2fe0 = MapGroup {
                members: list2[string] = {
                    "d787ef03-0198-4ece-ae4a-d9cc712d3c6c"
                    "81b1534d-ca73-440f-8ca5-02757951b8e2"
                    "069c2d78-46e7-4855-b280-6209ddb397c9"
                    "d7e9adef-f9eb-46dd-bcca-d33ada81b01f"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    747.372558, -188.900925, 2713.05542, 1
                }
                name: string = "group1"
            }
            0x929af03a = null
            0x70d30e6d = null
            0x62e28492 = null
            0xb17bb11f = null
            0x4d2e4d42 = null
            0x10e248dc = null
            0x0966fc44 = null
            0xeef3cf50 = null
            0x07a83356 = null
            0xdbf79be6 = null
            0x7698569d = null
            0x7eab9c54 = null
            0x6907fec2 = null
            0x1440def1 = null
            0x1d809b30 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship_Skybox" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x15348301 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Skybox_Spaceship_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2018.65112, 0.000122070312, 2112.27686, 1
                }
                name: string = "TFT_Skybox_Space_A1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship_Skybox"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Spaceship" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x69dc4859 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 2.03461576
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1932.31567, 679.710449, 1102.53369, 1
                }
                name: string = "Light_Red_01_7"
            }
            0x4818667a = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2506.0957, 804.190735, 115.258636, 1
                }
                name: string = "Light_Point_Center_DragonCloud1"
            }
            0x2213a1cd = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.70760596
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2041.19287, 339.757172, 2945.96973, 1
                }
                name: string = "Light_Red_01_9"
            }
            0x4db58880 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.87811923
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1074.00928, 460.003113, 2883.47925, 1
                }
                name: string = "Light_Red_01_10"
            }
            0x379bcc21 = MapPointLight {
                type: link = 0x45dda18a
                radiusScale: f32 = 1.18141556
                intensityScale: f32 = 1.39999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1989.89697, 486.53125, 2044.33398, 1
                }
                name: string = "Light_Green_01_2"
            }
            0x7543529e = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    555.900269, -388.330383, 1879.703, 1
                }
                name: string = "Freljord_FG_Torch5"
            }
            0x7cdfc6e7 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.939920306
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3210.48438, -388.330383, 3305.84351, 1
                }
                name: string = "Freljord_FG_Torch6"
            }
            0x47d34236 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3401.30615, -388.330383, 2370.31909, 1
                }
                name: string = "Freljord_FG_Torch11"
            }
            0x49a5eb0d = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2963.86108, -68.0293045, 1148.15906, 1
                }
                name: string = "Freljord_FG_Torch13"
            }
            0xe7589cc5 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2198.21289, -388.330383, 779.626587, 1
                }
                name: string = "Freljord_FG_Torch14"
            }
            0x82f7991a = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    842.518311, -388.330383, 813.353394, 1
                }
                name: string = "Freljord_FG_Torch15"
            }
            0x7c0177a8 = MapPointLight {
                type: link = 0x553c4952
                radiusScale: f32 = 0.866750658
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1152.33276, 449.460236, 1452.76123, 1
                }
                name: string = "Light_Point_Brazier_DragonCloud4"
            }
            0x24f3fde3 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.939920366
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1850.64136, -388.330383, 3521.35474, 1
                }
                name: string = "Freljord_FG_Torch16"
            }
            0x95154e2f = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.335597128
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    892.993286, 180.64473, 1313.54553, 1
                }
                name: string = "Odyssey_LightBlue_Fill5"
            }
            0x280492d7 = MapPointLight {
                type: link = 0x553c4952
                radiusScale: f32 = 0.866750658
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2863.67993, 449.460236, 2649.23511, 1
                }
                name: string = "Light_Point_Brazier_DragonCloud1"
            }
            0x16df9f08 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2296.71387, -75.6720886, 636.627869, 1
                }
                name: string = "Teal_Point_A1"
            }
            0xedddb777 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    786.871094, 199.036346, 2617.13403, 1
                }
                name: string = "Teal_Point_A2"
            }
            0xa1fcea5d = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    645.399719, -75.6720886, 769.502563, 1
                }
                name: string = "Teal_Point_A3"
            }
            0x9a2c9676 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2845.43994, -75.6720886, 3447.42969, 1
                }
                name: string = "Teal_Point_A4"
            }
            0x520717c3 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2066.27026, -75.6720886, 3638.74927, 1
                }
                name: string = "Teal_Point_A5"
            }
            0x8107a8e0 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1436.94263, -75.6720886, 636.627869, 1
                }
                name: string = "Teal_Point_A6"
            }
            0x7411a4f5 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3415.98584, 183.531982, 2109.86328, 1
                }
                name: string = "Teal_Point_A7"
            }
            0xd0709a84 = MapPointLight {
                type: link = 0x71b5db70
                radiusScale: f32 = 1.17450345
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    786.871094, 199.036346, 1888.52466, 1
                }
                name: string = "Teal_Point_A8"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Spaceship"
    }
    "Maps/MapGeometry/Map22/Galaxy_Spaceship" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Galaxy_Spaceship"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.34117648, 0.266666681, 0.529411793, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.482352942, 0.521568656, 0.741176486, 1 }
                horizonColor: vec4 = { 0.41568628, 0.372549027, 0.666666687, 1 }
                groundColor: vec4 = { 0.474509805, 0.286274523, 0.509803951, 1 }
                skyLightScale: f32 = 1
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 0.850000024
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Galaxy_Spaceship/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/SPACESHIP_NAVMESH.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0x3de2892b = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_Spaceship"
            0x83c20ac9 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_Spaceship"
            0x3601734b = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_Spaceship"
            0x1172c7a4 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship"
            0xcfb99647 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spaceship_Skybox"
            0xe36b6041 = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_Spaceship"
            "Galaxy_Design_Base_v2" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base_v2"
        }
    }
    "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Amb" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_Spaceship_Amb"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Amb"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spaceship_amb"
    }
    "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Skybox_Spaceship_A" = VfxSystemDefinitionData {
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
                        constantValue: vec3 = { 0, -150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = -10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Stars01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00400000019, 0 }
                }
                texDiv: vec2 = { 2, 2 }
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
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_MidgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.360006094, 0.889997721, 0.300007641 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.469993144, 0.76000613, 0.220004573 }
                }
                pass: i16 = -8
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.270000011, 0.270000011, 0.270000011 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_BlueCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                texDiv: vec2 = { 1, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 2 }
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
                emitterName: string = "Pink01"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.859998465, 0.540001512, 1, 0.340001523 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.889997721, 1 }
                }
                pass: i16 = -7
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
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
                emitterName: string = "Pink02"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.200000003, 0.990005314, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349996179, 0.910002291, 1, 0.420004576 }
                }
                pass: i16 = -6
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
                uvScaleMult: embed = ValueVector2 {
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
                emitterName: string = "Glow"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 150, -10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1.29999995, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds_B.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.972549021, 0.972549021, 0.972549021, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.541176498, 0.956862748, 1 }
                }
                pass: i16 = -9
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 0.170000002, 0.170000002 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_Clouds_Glow.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_BlueCloud_Mask.dds"
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
                emitterName: string = "Asteroid_A"
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
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Set2_Spaceship/FloatingAsteroid_A.TFT_ArenaSkin_Galaxy2.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.850980401, 0.580392182, 0.807843149, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.894117653, 0.721568644, 0.835294127, 1 }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0350000001, 0 }
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
                emitterName: string = "Asteroid_B"
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
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Set2_Spaceship/FloatingAsteroid_B.TFT_ArenaSkin_Galaxy2.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.792156875, 0.627451003, 0.768627465, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.760784328, 0.933333337, 1 }
                }
                pass: i16 = 7
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
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
                emitterName: string = "Asteroid_C"
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
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Set2_Spaceship/FloatingAsteroid_C.TFT_ArenaSkin_Galaxy2.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.615686297, 0.815686285, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.847058833, 0.980392158, 1 }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_FloatingRocks.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00899999961, 0 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_Spaceship_A"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Skybox_Spaceship_A"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 13
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
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
                            13
                        }
                    }
                }
                emitterName: string = "Wind"
                importance: u8 = 0
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Wind_Mesh.TFT_Freljord.scb"
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
                                    0.800000012
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
                                    0.800000012
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
                    constantValue: vec4 = { 1, 0.510002315, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.510002315, 1, 0 }
                            { 1, 0.510002315, 1, 0.800000012 }
                            { 1, 0.510002315, 1, 0 }
                        }
                    }
                }
                pass: i16 = 60
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 1, 30 }
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
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 1, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Wind_Wisp.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.200000003, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    -0.100000001
                                    0.100000001
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.200000003, 0.200000003 }
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
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Unitcombination_Backdrop_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            { -0.100000001, 0.100000001 }
                        }
                    }
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
        visibilityRadius: f32 = 6000
        particleName: string = "TFT_Spaceship_Wind"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Wind"
    }
    "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Arena_JetThruster01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.29999995
                }
                emitterName: string = "Aura_"
                disabled: bool = true
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Sona_Skin06_Genre03_aura_02.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.850980401, 0.254901975, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.850000024
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
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.920000017, 0.920000017 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Sona_Skin06_Genre03_Aura_2.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.0784313753, 0.172549024, 0.588235319, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0.800000012 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Sona_Skin06_Genre03_Aura_2.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.800000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "DJ_Shield_Thin"
                disabled: bool = true
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Sona_Skin06_Genre03_shield_full.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.29999995, 1.29999995 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Sona_Skin06_Genre03_Aura_2.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.0196078438, 0, 0.592156887, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.300000012 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Sona_Skin06_Genre03_Aura_2.dds"
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
                            { 1, 1, 1, 1 }
                            { 0.160784319, 0.286274523, 1, 1 }
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
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "TeamCircle"
                disabled: bool = true
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Base_burrowed_tremor_ring.TFT_Set5_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8.25, 25, 25 }
                }
                texture: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Ult_Aoe_04.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0 }
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
                            { 0.150000006, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.449999988 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "constantAdditiveAOE"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.333333343, 0.600000024, 1, 0.701960802 }
                }
                pass: i16 = 12
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 700, 500, 500 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/ShieldRing.dds"
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
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    0.949999988
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
                    constantValue: vec4 = { 1, 0.968627453, 0.490196079, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.968627453, 0.490196079, 0 }
                            { 1, 0.968627453, 0.490196079, 1 }
                            { 1, 0.968627453, 0.490196079, 0 }
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
                        constantValue: vec3 = { 7, 0, 0 }
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
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                emitterName: string = "up_glow"
                disabled: bool = true
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_expo_cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.670588255, 1, 0.450980395 }
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
                            { 0.121568628, 0.305882365, 0.709803939, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
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
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 5, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
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
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
                textureMult: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Trail_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
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
                texDivMult: vec2 = { 1, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    20
                }
                emitterName: string = "up_glow1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_expo_cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.930006862 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.262745112, 0.70588237, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.262745112, 0.70588237, 1, 0 }
                            { 0.262745112, 0.70588237, 1, 1 }
                            { 0.262745112, 0.70588237, 1, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
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
                            { 0, 180, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 2, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 16
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
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
                textureMult: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Trail_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
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
                texDivMult: vec2 = { 1, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                isSingleParticle: flag = true
                emitterName: string = "up_glow2"
                disabled: bool = true
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_expo_cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.298039228, 0.733333349, 1, 0.450980395 }
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
                            { 0.13333334, 0.509803951, 0.709803939, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
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
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
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
                    constantValue: vec3 = { 5, 3, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 0.5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/alpha_02.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 4
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
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
                textureMult: string = "ASSETS/Characters/Riven/Skins/Skin16/Particles/Riven_Skin16_Q_Trail_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
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
                texDivMult: vec2 = { 1, 3 }
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
                emitterName: string = "up_glow3"
                disabled: bool = true
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Galaxy_Center_Island_Gate.TFT_Set3.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.31764707, 1, 1 }
                }
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/GalaxyGate_VFXTexture_all.TFT_Set3.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.125, 0 }
                }
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
                emitterName: string = "up_glow4"
                disabled: bool = true
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -10, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Galaxy_Center_Island_Gate.TFT_Set3.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0627451017, 0.470588237, 1, 1 }
                }
                pass: i16 = -1
                disableBackfaceCull: bool = true
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/GalaxyGate_VFXTexture.TFT_Set3.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.125, 0 }
                }
                texDiv: vec2 = { 0.0769999996, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
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
                emitterName: string = "Lightning_AOE_Ring"
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 350, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 350, 0 }
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
                    constantValue: vec4 = { 0.41568628, 0.670588255, 1, 0.792156875 }
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
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
                            { 0.41568628, 0.670588255, 1, 0 }
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
                            { 0.41568628, 0.670588255, 1, 0.792156875 }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 225, 750, 225 }
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
                        values: list[vec3] = {
                            { 225, 750, 225 }
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
                            { 1, 1, 1 }
                            { 1, 1, 1 }
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
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
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
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 275, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 275, 0 }
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
                    constantValue: vec4 = { 0.447058827, 0.741176486, 1, 0.792156875 }
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
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
                            { 0.447058827, 0.741176486, 1, 0 }
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
                            { 0.447058827, 0.741176486, 1, 0.792156875 }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 225, 750, 225 }
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
                        values: list[vec3] = {
                            { 225, 750, 225 }
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
                            { 1, 1, 1 }
                            { 1, 1, 1 }
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
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.519999981
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
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 225, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 225, 0 }
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
                    constantValue: vec4 = { 0.380392164, 0.764705896, 1, 0.792156875 }
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
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
                            { 0.380392164, 0.764705896, 1, 0 }
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
                            { 0.380392164, 0.764705896, 1, 0.792156875 }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 225, 750, 225 }
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
                        values: list[vec3] = {
                            { 225, 750, 225 }
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
                            { 1, 1, 1 }
                            { 1, 1, 1 }
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
                    constantValue: vec4 = { 0.309803933, 0.666666687, 1, 0.360784322 }
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
                depthBiasFactors: vec2 = { 1, 10 }
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
                    constantValue: f32 = 0.75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "Temp_GroundGlow1"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
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
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
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
                disabled: bool = true
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
                    constantValue: vec4 = { 0.631372571, 0.419607848, 1, 0.541176498 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.631372571, 0.419607848, 1, 0 }
                            { 0.631372571, 0.419607848, 1, 0.541176498 }
                            { 0, 0.00493656285, 0.721568644, 0.541176498 }
                            { 0.00495194178, 0, 0.56078434, 0 }
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
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.25
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    0.949999988
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
                    constantValue: vec4 = { 1, 1, 0.447058827, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0.447058827, 0 }
                            { 1, 1, 0.447058827, 1 }
                            { 1, 1, 0.447058827, 0 }
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
                        constantValue: vec3 = { 7, 0, 0 }
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
                    constantValue: f32 = 3
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
                                    0.75
                                    1.25
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
                    12
                }
                emitterName: string = "Temp_GroundGlow2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 300, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.409994662, 0.639993906, 1, 0.689997733 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.409994662, 0.639993906, 1, 0 }
                            { 0.409994662, 0.639993906, 1, 0.689997733 }
                            { 0.409994662, 0.639993906, 1, 0.689997733 }
                            { 0.409994662, 0.639993906, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 1000, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 2, 0.5, 0 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set5.dds"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: string = "ASSETS/Shared/Particles/Base_Comet_Impact_Smoke.LittleLegends_10_10.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 0 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                                    0.75
                                    1.25
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
                    12
                }
                emitterName: string = "Temp_GroundGlow3"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 400, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.179995418, 0.650003791, 1, 0.439993888 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.179995418, 0.650003791, 1, 0 }
                            { 0.179995418, 0.650003791, 1, 0.439993888 }
                            { 0.179995418, 0.650003791, 1, 0.439993888 }
                            { 0.179995418, 0.650003791, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 1000, 50 }
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
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
        }
        particleName: string = "TFT_Spaceship_Arena_JetThruster01"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Spaceship_Arena_JetThruster01"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Thrusters" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_Spaceship_Thrusters"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Spaceship/TFT_Audio-Emitter_Galaxy_Spaceship_Thrusters"
        soundOnCreateDefault: string = "Play_sfx_tft_env_galaxy_spaceship_thrusters_spark"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spaceship_thrusters"
    }
    "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_common_amb_loop"
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
    0x45dda18a = MapPointLightType {
        lightColor: vec4 = { 0.784313738, 0.729411781, 0.505882382, 1 }
        radius: f32 = 1100
        specular: bool = false
        Impact: i32 = 1
    }
    0x4ddca076 = MapPointLightType {
        radius: f32 = 800
        Impact: i32 = 1
    }
    0x553c4952 = MapPointLightType {
        lightColor: vec4 = { 0.870588243, 1, 1, 1 }
        radius: f32 = 800
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x52248cce = MapPointLightType {
        lightColor: vec4 = { 0.690196097, 0.227450982, 0.772549033, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x534460ea = MapPointLightType {
        lightColor: vec4 = { 0.866666675, 0.80392158, 0.443137258, 1 }
        specular: bool = false
        Impact: i32 = 1
    }
    0x62a42502 = MapPointLightType {
        lightColor: vec4 = { 0.494117647, 0.917647064, 0.921568632, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x71b5db70 = MapPointLightType {
        lightColor: vec4 = { 0, 0.494117647, 0.56078434, 1 }
        Impact: i32 = 1
    }
}
