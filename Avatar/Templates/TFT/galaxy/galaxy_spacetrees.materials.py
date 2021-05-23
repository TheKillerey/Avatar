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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Flower_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Flower_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SpaceTrees_Flower_B.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_SpaceTrees_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_SpaceTrees_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Board_SpaceTrees_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Plant_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Plant_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SpaceTrees_Plant_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Bush_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Bush_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SpaceTrees_Bush_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Leaf_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Leaf_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SpaceTrees_Leaf_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Flower_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/SpaceTrees_Flower_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SpaceTrees_Flower_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Missile_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Missile_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Missile_A.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Birds" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Birds"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Birds"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_birds"
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tree_Branches" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Tree_Branches"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tree_Branches"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_trees_wind"
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tones_Meditation" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Tones_Meditation"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tones_Meditation"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_tones_meditation"
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Skybox_SpaceTrees_A" = VfxSystemDefinitionData {
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
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.282352954, 0.97647059, 0.709803939, 1 }
                }
                pass: i16 = -10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Stars01.dds"
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
                    constantValue: vec4 = { 1, 0.289997697, 0.710002303, 0.269993126 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.474509805, 0.75686276, 0.650980413 }
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
                    constantValue: vec4 = { 0.200000003, 0.764705896, 0.772549033, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.337254912, 0.568627477, 0.576470613, 1 }
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
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_SpaceTrees_A"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Skybox_SpaceTrees_A"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Crickets" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Crickets"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Crickets"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_crickets"
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Chimes_Clang" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Chimes_Clang"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Chimes_Clang"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_chimes_clang"
    }
    "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Fountain_Water" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Fountain_Water"
        particlePath: string = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Fountain_Water"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_spacetrees_fountain_water"
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
    "Maps/Particles/TFT/Galaxy/CrashSite/Galaxy_Blackhole_Wind" = VfxSystemDefinitionData {
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
                isLocalOrientation: flag = false
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
        particleName: string = "Galaxy_Blackhole_Wind"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/Galaxy_Blackhole_Wind"
        flags: u8 = 197
    }
    "Maps/MapGeometry/Map22/Galaxy_SpaceTrees" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Galaxy_SpaceTrees"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.34117648, 0.266666681, 0.529411793, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.482352942, 0.521568656, 0.741176486, 1 }
                horizonColor: vec4 = { 0.321568638, 0.286274523, 0.509803951, 1 }
                groundColor: vec4 = { 0.368627459, 0.219607845, 0.392156869, 1 }
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
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Galaxy_SpaceTrees/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Galaxy_SpaceTrees_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            "Galaxy_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base"
            0x32425435 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared"
            0x99cfb88e = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_SpaceTrees"
            0xf97c8114 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_SpaceTrees"
            0x0fff7b2e = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_SpaceTrees"
            0xa31c8a9c = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_SpaceTrees"
            0x39431e73 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_SpaceTrees"
            0x0edfe87d = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spacetree_Skybox"
        }
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_SpaceTrees" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf6241972 = MapLightingVolume {
                sunColor: vec4 = { 0.470588237, 0.666666687, 0.70588237, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                0xba02f116: f32 = 0.100000001
                skyLightColor: vec4 = { 0.309803933, 0.466666669, 0.490196079, 1 }
                horizonColor: vec4 = { 0.321568638, 0.352941185, 0.494117647, 1 }
                groundColor: vec4 = { 0.227450982, 0.286274523, 0.325490206, 1 }
                skyLightScale: f32 = 0.5
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.0980392173, 0.0862745121, 0.200000003, 1 }
                fogAlternateColor: vec4 = { 0.0588235296, 0.188235298, 0.266666681, 1 }
                fogStartAndEnd: vec2 = { 250, -600 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2186.59424, -927.355957, 2144.35596, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_SpaceTrees"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spacetree_Skybox" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x7c47941d = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Skybox_SpaceTrees_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2018.05859, -0.000244140625, 2107.80713, 1
                }
                name: string = "TFT_Skybox_SpaceTrees_A1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Spacetree_Skybox"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2ff7cdaf = null
            0x280cca76 = null
            0x8428f883 = null
            0xe30670d4 = null
            0x2b87a377 = null
            0xbb931b41 = null
            0x4cbd628a = null
            0x42024cef = null
            0x53ed22c7 = null
            0x094349ef = null
            0xb1d8cef4 = null
            0xf4b61a8f = null
            0xab595e64 = null
            0x05717daa = null
            0x329adcec = null
            0x79acf00c = null
            0xf043b4b5 = null
            0xd6d5733c = null
            0xa8d44455 = null
            0x019b834d = null
            0x1d77da53 = null
            0xb7e917a0 = null
            0x9297418f = null
            0x3b47d4bd = null
            0x17bc3116 = null
            0xee65b0c2 = null
            0x35a36457 = null
            0xeff8da4b = null
            0x7a3df143 = null
            0x5d77c8c4 = null
            0x1a238f12 = null
            0xfe47d27d = null
            0x56565a88 = null
            0x5ca62bc1 = null
            0xc1006eb1 = null
            0x9bd2715d = null
            0x30c93fa1 = null
            0x7d0e7eab = null
            0x3cd8e0f7 = null
            0x42e3d592 = null
            0xbb52d822 = null
            0x3467a2ff = null
            0xb4c99a87 = null
            0x20ca2a2c = null
            0x5b9cd197 = null
            0x434c84c3 = null
            0x52bbeec2 = null
            0x41c52df6 = null
            0x7399c8da = null
            0xefebf928 = null
            0x7551669f = null
            0x6158c9cf = null
            0x2a7774db = null
            0xa4682294 = null
            0x35e6a257 = MapGroup {
                members: list2[string] = {
                    "c451d051-0d2c-4840-91db-65cfd0df1ec1"
                    "26320d51-b0c6-4d9e-adcd-c3d70889d47d"
                }
                name: string = "group15"
            }
            0x44ff912f = null
            0x3e7970d3 = null
            0x25191500 = null
            0xd4fe640a = MapGroup {
                members: list2[string] = {
                    "73947327-75ac-4800-a52d-47e55caf6a79"
                    "9b30e97a-0edf-4cc1-8a73-3cf21c10dd03"
                    "8baed65f-fb57-4b67-ac97-06a00c57a686"
                    "ce2b35da-f683-4a24-8e5c-c34d4dcb6230"
                }
                name: string = "group19"
            }
            0x5ceac25e = null
            0xca57d935 = null
            0xd675623d = null
            0x7472518f = null
            0xc09e1860 = null
            0x3b78fc17 = null
            0x55126cee = null
            0xbbbf5dc0 = null
            0x757650c5 = null
            0xbf1f198e = null
            0xfaef2fbb = null
            0xe855532b = null
            0x920c4873 = null
            0xfcceb49c = null
            0xd7472490 = null
            0x38c82321 = null
            0x59e7c7ef = null
            0xa632e126 = null
            0x4a3bc502 = null
            0xebb4e9b7 = null
            0x649d4d0c = null
            0xba60e39c = null
            0xa8f7297b = null
            0xb9c1383c = null
            0x8f60e8ce = null
            0xbb0e8c04 = null
            0x50442457 = null
            0x537b4715 = null
            0x59c7108b = null
            0x60bc0146 = null
            0xe525996b = null
            0x13d941ee = null
            0x453319f6 = null
            0x6c4a33d5 = null
            0x302c2c48 = null
            0x142d9399 = null
            0x67613649 = null
            0x29d03e8c = null
            0x11763954 = null
            0xe6806b2a = null
            0x4eec50de = null
            0xec7ee90d = null
            0x245334ad = null
            0x5d148095 = null
            0xb8b46272 = null
            0xb19fcaf8 = null
            0xebe9512f = null
            0x953ab1a9 = null
            0xc71b37f3 = null
            0x1d409379 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 0.948094666, 0
                    2995.67822, -339.70752, 2667.89282, 1
                }
                name: string = "group1"
            }
            0x9093d129 = null
            0x45fb23c1 = null
            0xe873784e = null
            0x91603791 = null
            0x3fdf3804 = null
            0xb3299236 = null
            0x235b2294 = null
            0xcc475dcc = null
            0x53aae39c = null
            0xe4b79064 = null
            0xe89a5db0 = null
            0x235bf9ba = null
            0xc7537449 = null
            0xd248423b = null
            0x7353ff5b = null
            0x118a5998 = null
            0x6ef00b3d = null
            0x4fda4f08 = null
            0x2a763665 = null
            0x43bd56ab = null
            0x92469741 = null
            0xc4925fe5 = null
            0x12302de6 = null
            0x3b720783 = null
            0xd8d13bb3 = MapGroup {
                members: list2[string] = {
                    "23ab19f5-6c49-46c8-83c5-474913178f5c"
                    "eb1f8eed-3f53-4fd7-81f1-a30cddf7626f"
                    "a35e5b65-ce0e-459d-a63e-dab864818dcb"
                    "e10cb0a9-4f41-4577-96f1-28d6648e42f2"
                    "7443d31c-69a4-40eb-b899-cfe065714df9"
                    "5e1ba055-eb3d-4a37-b29c-13cceff43f26"
                    "36ba2e5f-890e-4fb2-95ce-12883f3b0275"
                    "64944ff3-77cf-43a0-a53b-433d306ce246"
                    "e000be44-9aa7-4e63-a027-9fdcfece4a64"
                    "a5c3ec42-64cf-458b-a973-d692cb93f30c"
                }
                transform: mtx44 = {
                    -3.57627869e-07, 0, 1, 0
                    0, 1, 0, 0
                    -1, 0, -3.57627869e-07, 0
                    1699.83521, -118.505661, 409.408142, 1
                }
                name: string = "group5"
            }
            0xa6f078fa = null
            0xadd350c9 = null
            0x56b79bfe = null
            0xbc4d3603 = null
            0x9c6278b9 = null
            0xcf2d26a9 = null
            0x1c3b32ad = null
            0x4594fd09 = null
            0xbd178575 = null
            0x70bd1a2e = null
            0xd17f1116 = null
            0x7ca7fe0f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_SpaceTrees" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x71e0fcf3 = MapGroup {
                members: list2[string] = {
                    "46c4e82a-67ba-4480-ab8a-82092b36a846"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group2"
            }
            0xedd92efb = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1040.97327, 11.4734955, 2034.53284, 1
                }
                name: string = "group3"
            }
            0xe3b0a75e = MapGroup {
                members: list2[string] = {
                    "ae05c230-0317-45d2-b083-b9f98ada78e2"
                    "f3da4638-b4db-4f1d-b1f4-43342592c6b6"
                    "e5abdaaa-a125-4834-a5d9-878bf6900f34"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group4"
            }
            0x72cf66ae = MapGroup {
                transform: mtx44 = {
                    -0.999021709, 0, -0.0442254655, 0
                    0, 1, 0, 0
                    0.0442254655, 0, -0.999021709, 0
                    2308.2771, -6.97145081, 1343.43469, 1
                }
                name: string = "group10"
            }
            0x5371f181 = MapGroup {
                members: list2[string] = {
                    "bbcd36a7-4271-4a2f-aef8-145e9347008c"
                    "97e00e46-2688-4fab-ac0d-c86d2063958a"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group11"
            }
            0x59c1f181 = MapGroup {
                members: list2[string] = {
                    "5eef191d-c8dd-4958-aa3f-6ca0e84694b3"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group12"
            }
            0x16a8a759 = MapGroup {
                members: list2[string] = {
                    "78bf7cb5-6c90-418b-be6b-dd99201658d8"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group13"
            }
            0x1b49f480 = MapGroup {
                members: list2[string] = {
                    "4beb422b-1c09-4da8-838d-eb424ca3e571"
                    "c1d9881d-68ef-4f66-a98a-2a800fbb461b"
                    "6548d539-e0f7-4099-a46d-c52ddc8ae2d7"
                    "8845290f-77dd-4e26-879b-7f9f4d298850"
                    "6b3286b4-3926-466f-bd2a-fc95676b07e1"
                    "54fde7de-c944-4949-b431-94f60487ed27"
                    "4cfbc540-7a66-4dce-808d-95d09c3cb804"
                    "dca82d86-af08-4ba8-926e-14fe0378b72b"
                    "edcafcd6-3d19-40c8-a08b-5cbb669e279e"
                    "eecd2c90-4cd7-419b-9b78-e44329454fe1"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group14"
            }
            0x1a4334e2 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2109.7439, -9.59887695, 3723.11792, 1
                }
                name: string = "group16"
            }
            0x3a2d813a = MapGroup {
                transform: mtx44 = {
                    -0.350199789, 0, -0.93667537, 0
                    0, 1, 0, 0
                    0.93667537, 0, -0.350199789, 0
                    2480.68188, -16.2309723, 1465.65747, 1
                }
                name: string = "group17"
            }
            0xcd14b579 = MapGroup {
                members: list2[string] = {
                    "dbbef700-f182-44e5-9b99-ff2212749ec5"
                    "ad2d7532-b2f7-4fc8-bb81-450911447c0d"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group18"
            }
            0x8d688acc = MapGroup {
                members: list2[string] = {
                    "955b2790-99c5-4687-825e-edf132b1e9fb"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group20"
            }
            0x5b98f201 = MapGroup {
                transform: mtx44 = {
                    0.914000273, 0, -0.405715406, 0
                    0, 1, 0, 0
                    0.405715406, 0, 0.914000273, 0
                    3340.31812, -9.81459045, 3288.66675, 1
                }
                name: string = "group21"
            }
            0xc5eb3976 = MapGroup {
                members: list2[string] = {
                    "672276aa-154a-4408-9ab0-0583726067c9"
                    "1f8923f9-1251-4512-bf02-0494dbbbb5dd"
                    "9c72125c-0fac-4eb8-acb4-ae9ebb67cbd9"
                    "b19a7d1f-8e2b-4d9d-add3-6f0819466c54"
                    "7012f17d-ead5-4dc5-928c-9e2bc7317a53"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group22"
            }
            0xa8278b7c = null
            0x9a8b01f3 = null
            0x70b03f00 = null
            0xf20016cd = null
            0x311ce6bc = null
            0x7314057e = null
            0x86568eb0 = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1039.13831, 11.0271511, 2041.48511, 1
                }
                name: string = "group23"
            }
            0xac745207 = MapGroup {
                members: list2[string] = {
                    "efb47d7e-e71c-4398-8171-cb9a55183cd0"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group24"
            }
            0xbad2740c = MapGroup {
                members: list2[string] = {
                    "42c93de6-91dc-4574-bcea-9dda240b97d3"
                    "b655e188-c281-4af6-a3f8-b67e10054369"
                    "4cf86c8f-7809-4f1b-95e0-9f45a743ea2d"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group25"
            }
            0xa54b788a = MapGroup {
                members: list2[string] = {
                    "8cd6db5f-ea16-4e39-b3e6-2bc7dc7bdb57"
                    "ef358af1-5c6e-4510-b0a7-43c13802646d"
                    "f05ac316-ad0e-4772-8bda-fadae1f18d9d"
                    "69e3adf5-ffb5-40ac-b7d8-29246e096c72"
                    "113ffd64-163b-4fcd-ac20-65e4a3c5d624"
                    "a1165856-58c7-496a-930e-f4a5e11dd092"
                    "fb5c5943-4441-4e32-83a5-b176359c00fd"
                    "6a77d96b-ed5d-4038-942b-18f97ee885af"
                    "1bb52b1d-6d82-4bb9-be43-fdb7b50bc8cf"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -4.36231995, 0, 1
                }
                name: string = "group26"
            }
            0x2d1a7d40 = null
            0x38801a97 = MapGroup {
                transform: mtx44 = {
                    0.780005276, 0, 0, 0
                    0, 0.780005276, 0, 0
                    0, 0, 0.780005276, 0
                    3432.7168, -4.36256409, 1315.96899, 1
                }
                name: string = "group27"
            }
            0x44fd4a96 = null
            0x18e5909f = null
            0xfd7f1099 = null
            0xc00cd1ee = null
            0xfc4995fc = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    2657.81104, -224.218735, 4405.47168, 1
                }
                name: string = "group28"
            }
            0xcee6b4fe = null
            0x9cfe015f = null
            0x6b51d6e1 = null
            0xe189d4e8 = null
            0x9622426d = null
            0x0205ef16 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 0.943893969, 0
                    2768.62793, -3.94784808, 1141.61133, 1
                }
                name: string = "group6"
            }
            0x8cf6951a = null
            0xf51595a0 = null
            0x09e6eb8c = null
            0x9a4b104f = null
            0xe366417c = null
            0xb68f5566 = null
            0x5237cf6c = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2491.72388, -19.7436333, 1051.06116, 1
                }
                name: string = "group7"
            }
            0x6396c70f = null
            0xf1989cd1 = null
            0x6a874e56 = null
            0xfe5a9f4d = null
            0x31f8f66d = null
            0x11acce61 = null
            0xac3c94a0 = null
            0xadbb0d5a = null
            0x395e877e = null
            0xd886155c = null
            0xc0807f79 = null
            0xada405ff = MapGroup {
                members: list2[string] = {
                    "0e3ba4b2-889f-4d09-a631-7e0dec436f81"
                    "07159711-7f07-4f92-9ad1-6ad891dc9a06"
                }
                transform: mtx44 = {
                    0.658126593, -0.0502897874, 0, 0
                    0.048117768, 0.629701972, -0.191884652, 0
                    0.014619966, 0.191326872, 0.631537735, 0
                    3312.09228, -86.4964905, 1822.14905, 1
                }
                name: string = "group8"
            }
            0xc913ed75 = MapGroup {
                members: list2[string] = {
                    "cb50f105-c238-4d24-8ed0-c4a4d575ab1f"
                }
                transform: mtx44 = {
                    0.999561727, 0, 0, 0
                    0, 0.999561727, 0, 0
                    0, 0, 0.999561727, 0
                    3139.60229, -114.596352, 1392.53699, 1
                }
                name: string = "group9"
            }
            0xa86728e4 = null
            0xbeb19a89 = null
            0xa3d2c0ea = null
            0x5cff05e5 = null
            0x1917af4c = null
            0xf4bd0789 = MapGroup {
                members: list2[string] = {
                    "3a46b200-bb8e-42fe-8f01-4dc5d46ab40d"
                }
                transform: mtx44 = {
                    0.59238857, 0, -1.24940908, 0
                    0, 1.38273168, 0, 0
                    1.24940908, 0, 0.59238857, 0
                    2818.27173, -193.471771, 531.867432, 1
                }
                name: string = "group30"
            }
            0x67e98082 = null
            0x703a07c1 = MapGroup {
                members: list2[string] = {
                    "3d5d3eb6-b342-416b-b7f9-8ec7d4cf35e6"
                    "e674ef11-cdbb-4cc1-a14c-d76c9bc9db59"
                }
                transform: mtx44 = {
                    0.82636565, 0, 0, 0
                    0, 0.82636565, 0, 0
                    0, 0, 0.82636565, 0
                    575.248169, -146.409668, 1206.06287, 1
                }
                name: string = "group29"
            }
            0xdfa221f9 = null
            0x299ef6da = null
            0xf5eb4093 = null
            0x6e261d2b = null
            0x12e7c3ab = null
            0x61e608f6 = MapGroup {
                members: list2[string] = {
                    "dc1a89d1-7d29-4cf4-94ae-3c15368e7783"
                }
                transform: mtx44 = {
                    1.09137607, 0, 0.21148847, 0
                    0, 1.11167848, 0, 0
                    -0.21148847, 0, 1.09137607, 0
                    609.453064, -242.157654, 1153.60669, 1
                }
                name: string = "group31"
            }
            0x53097b39 = MapGroup {
                members: list2[string] = {
                    "0fc497f3-0bcf-4aba-92c7-9c330b65373e"
                    "8deb3e92-9d39-4976-90d0-bef866243d2c"
                }
                transform: mtx44 = {
                    0.33919847, -0.229536578, -0.575823009, 0
                    0.198992789, 0.661972642, -0.146657929, 0
                    0.587078393, -0.0917583182, 0.382405698, 0
                    3436.75562, -193.149979, 1693.66052, 1
                }
                name: string = "group32"
            }
            0x5d2a7eaa = null
            0x71b1bb35 = null
            0x1ae8e235 = null
            0x9a757408 = MapGroup {
                transform: mtx44 = {
                    0.858895719, 0, -0.512150526, 0
                    0, 1, 0, 0
                    0.512150526, 0, 0.858895719, 0
                    3552.11768, -642.924866, 1962.77649, 1
                }
                name: string = "group33"
            }
            0xeb7e8a99 = MapGroup {
                members: list2[string] = {
                    "cff9627e-2daa-4aa7-8496-edfd49c00465"
                    "bbe4546e-c99d-4bbf-9bbc-f4a0ca1e136e"
                    "d9e1bd4f-c700-498f-a490-56b16de88a15"
                    "ddfebe23-6fa8-4ea6-a1e7-6b36d2028e46"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1032.0636, -210.095139, 3397.29224, 1
                }
                name: string = "group34"
            }
            0xdc07299f = null
            0xce478699 = MapGroup {
                members: list2[string] = {
                    "3ec97120-47b4-4692-893f-a414f8712b69"
                    "d906332c-3bb3-4eda-b08e-0c1136ebd955"
                }
                transform: mtx44 = {
                    0.0922067091, 0.00701276259, -0.741140366, 0
                    -0.0566407554, 0.744736135, 0, 0
                    0.739006102, 0.0562049635, 0.0924730003, 0
                    2741.91064, -585.510742, 1040.78503, 1
                }
                name: string = "group36"
            }
            0x1d12fda8 = null
            0x8a0d0a52 = null
            0xe99971ae = MapGroup {
                members: list2[string] = {
                    "98d5177c-e9b9-42ef-b1b0-ffe96963676e"
                    "1d4dbb3a-5dd7-48a4-ac99-b901056488df"
                }
                transform: mtx44 = {
                    0.692456067, 0, 0.15598096, 0
                    0, 0.709806681, 0, 0
                    -0.15598096, 0, 0.692456067, 0
                    3315.27246, -390.500092, 3180.62573, 1
                }
                name: string = "group35"
            }
            0x5de6e106 = null
            0x2b1142bf = MapGroup {
                members: list2[string] = {
                    "0fc497f3-0bcf-4aba-92c7-9c330b65373e"
                }
                transform: mtx44 = {
                    0.285136193, 0, -0.649016023, 0
                    0, 0.708889544, 0, 0
                    0.649016023, 0, 0.285136193, 0
                    3239.09888, -662.51532, 1885.58203, 1
                }
                name: string = "group37"
            }
            0x11b24ef6 = null
            0x8b75fa58 = null
            0xccda5c52 = null
            0x1f3a2df7 = null
            0x5059a7c2 = null
            0x9b106cd8 = null
            0x22e8ef45 = null
            0x7266dfbd = null
            0x2950596d = null
            0x6626e2a7 = null
            0xc65a821c = null
            0x6a2564d2 = null
            0x5351ba0f = null
            0x62b8b4cb = null
            0x69a7047c = null
            0x597af113 = null
            0x75104190 = null
            0x63f43963 = null
            0xc27a70ed = null
            0x40dc3707 = null
            0x20720c63 = null
            0x02d1b276 = null
            0xc9e27ebe = null
            0xa45edc33 = null
            0xfbd521a8 = null
            0x889ab1c7 = null
            0x07c68aa5 = null
            0x92fbd136 = null
            0xe2ffc05e = null
            0xaeac2820 = null
            0xcdcd27ea = null
            0xe49b0e13 = null
            0x5de0d4e8 = null
            0x082c6fed = null
            0xbced36d4 = null
            0x27e4570a = null
            0x6076d31a = null
            0x629ce8e6 = null
            0x50fdc0ba = null
            0x0876e0e2 = null
            0xe66553f0 = null
            0xc2f100f3 = null
            0xe305496b = null
            0x1f88e9d2 = null
            0x4d24351e = null
            0x11705295 = null
            0x45b76a68 = null
            0xaacc7459 = null
            0xa2026937 = null
            0x547e1120 = null
            0x457e2d79 = null
            0x15f88c30 = null
            0xd820a67b = null
            0xc5ae944d = null
            0x8bbba15d = null
            0x00c8fba8 = null
            0x2502c7d9 = null
            0xed1ea1bd = null
            0x9b091444 = null
            0x138a8427 = null
            0x2310d463 = null
            0x21d50d55 = null
            0x403661b5 = null
            0xb74fb8ce = null
            0x4b3cc7f0 = null
            0x1cac8db9 = null
            0x39ab2bd3 = null
            0x081a84d8 = null
            0xddecc42a = null
            0xad77dbcc = null
            0x4c3e2bdf = null
            0x5f609602 = null
            0x1202083f = null
            0xa9d67607 = null
            0xcffa03bc = null
            0xb70120c2 = null
            0xecd12f2c = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_SpaceTrees"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_SpaceTrees" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x5f6c5873 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/Galaxy_Blackhole_Wind"
                colorModulate: vec4 = { 1, 1, 1, 0.459998488 }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1949.68848, -0.00048828125, 1474.64795, 1
                }
                name: string = "Galaxy_Blackhole_Wind1"
            }
            0xac9d5d45 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/Galaxy_Blackhole_Wind"
                colorModulate: vec4 = { 1, 1, 1, 0.560006082 }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2185.58325, -0.000610351562, 2444.10889, 1
                }
                name: string = "Galaxy_Blackhole_Wind2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_SpaceTrees"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base" = MapPlaceableContainer {
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
                    2995.97485, 0, 2859.89062, 1
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
                    943.477173, 0, 1180.83337, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_SpaceTrees" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa05e17b4 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.18850374
                intensityScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1967.97607, 345.161011, 1094.99988, 1
                }
                name: string = "Light_Point_Center_DragonCloud6"
            }
            0x606ba67c = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2506.0957, 804.190735, 115.258636, 1
                }
                name: string = "Light_Point_Center_DragonCloud8"
            }
            0x3c73c0c6 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.18722856
                intensityScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2054.1377, 345.161011, 2924.00732, 1
                }
                name: string = "Light_Point_Center_DragonCloud9"
            }
            0x86730e13 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.30712783
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3199.23413, -281.519684, 1589.18652, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean2"
            }
            0x4cf65409 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.58853686
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    486.489136, -281.519684, 2073.83984, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean5"
            }
            0x27706d15 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.36176133
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2550.35791, -281.519684, 3452.50903, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean6"
            }
            0x0fdb35dd = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.828923523
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3920.76416, 694.723144, 2957.46118, 1
                }
                name: string = "Freljord_FG_Torch4"
            }
            0x9b445519 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.625105798
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2559.88306, 443.686829, 3076.52978, 1
                }
                name: string = "Freljord_WC_Blue_Fill2"
            }
            0x8b43f691 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.853660226
                intensityScale: f32 = 0.649999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    128.597412, 694.723144, 1333.21973, 1
                }
                name: string = "Freljord_FG_Torch3"
            }
            0x2c54f4ab = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.910724699
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2864.77734, 354.603027, 2650.73389, 1
                }
                name: string = "Freljord_AV_Center3"
            }
            0xdebabc04 = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.910724699
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    502.733215, -80.6737366, 2087.71924, 1
                }
                name: string = "Freljord_AV_Center4"
            }
            0x86d272ce = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.693768144
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3628.03979, -80.6737366, 2379.66308, 1
                }
                name: string = "Freljord_AV_Center5"
            }
            0x95c6a2ba = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.882298231
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2048.40552, 366.479248, 3617.66113, 1
                }
                name: string = "Freljord_AV_Center6"
            }
            0x9831076b = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.422765642
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2033.07471, -19.3888779, 625.758057, 1
                }
                name: string = "Freljord_AV_Center7"
            }
            0xbac5b66b = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.549535334
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    293.221497, 318.160217, 2658.81201, 1
                }
                name: string = "Freljord_WC_Blue_Fill3"
            }
            0xbd326c51 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.843799591
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3455.31885, -212.221436, 1783.88086, 1
                }
                name: string = "Freljord_WC_Blue_Fill4"
            }
            0x337f41a4 = MapPointLight {
                type: link = 0x72e7702e
                radiusScale: f32 = 0.235070884
                intensityScale: f32 = 1.64999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2024.828, 481.291351, 2006.948, 1
                }
                name: string = "Light_Center_Point_DragonFire1"
            }
            0x954be16a = MapPointLight {
                type: link = 0x72e7702e
                radiusScale: f32 = 0.0946552381
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3055.41528, 803.67749, 1456.44897, 1
                }
                name: string = "Light_Center_Point_DragonFire2"
            }
            0xb919be4c = MapPointLight {
                type: link = 0x72e7702e
                radiusScale: f32 = 0.0921176374
                intensityScale: f32 = 0.649999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3256.53345, 615.749207, 3249.28906, 1
                }
                name: string = "Light_Center_Point_DragonFire3"
            }
            0x79014939 = MapPointLight {
                type: link = 0x72e7702e
                radiusScale: f32 = 0.100158148
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1139.82312, 631.655518, 3249.28906, 1
                }
                name: string = "Light_Center_Point_DragonFire4"
            }
            0xedd384aa = MapPointLight {
                type: link = 0x72e7702e
                radiusScale: f32 = 0.088401325
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3007.09961, 227.621399, 783.596558, 1
                }
                name: string = "Light_Center_Point_DragonFire5"
            }
            0xbfe52416 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.519084632
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    508.741272, -128.507278, 1705.72485, 1
                }
                name: string = "Freljord_WC_Blue_Fill5"
            }
            0x708309b1 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.687238753
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1313.1438, -128.507278, 467.884216, 1
                }
                name: string = "Freljord_WC_Blue_Fill6"
            }
            0xa6faebce = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.464914948
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3698.85742, -428.673584, 534.242981, 1
                }
                name: string = "Freljord_WC_Blue_Fill7"
            }
            0xe79b599f = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.488232046
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3927.81714, -131.703857, 3211.45435, 1
                }
                name: string = "Freljord_WC_Blue_Fill8"
            }
            0x0c91dc58 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 0.630196095
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    744.375366, 269.512787, 2737.88086, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth1"
            }
            0xa773c5d2 = null
            0x53506214 = null
            0x9cef856e = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.883696258
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3706.8335, -528.250488, 2048.30225, 1
                }
                name: string = "Freljord_FG_Torch1"
            }
            0x01f33091 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.788946688
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2012.15771, -528.250488, 467.574646, 1
                }
                name: string = "Freljord_FG_Torch2"
            }
            0x2777eebc = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.762845039
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2038.47363, -528.250488, 3650.17871, 1
                }
                name: string = "Freljord_FG_Torch5"
            }
            0xb62dc6fb = null
            0x0de87ee5 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.883696258
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3050.77222, -471.114197, 501.755981, 1
                }
                name: string = "Freljord_FG_Torch6"
            }
            0xcdf7ee52 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.76809597
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    539.471619, -471.114197, 501.755981, 1
                }
                name: string = "Freljord_FG_Torch7"
            }
            0x01d150e9 = MapPointLight {
                type: link = 0xdd24adc9
                radiusScale: f32 = 0.201276094
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    909.007385, 152.047684, 1455.21399, 1
                }
                name: string = "light_01_1"
            }
            0xbe1cb131 = MapPointLight {
                type: link = 0xdd24adc9
                radiusScale: f32 = 0.262739867
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    831.740845, 139.155838, 1318.95593, 1
                }
                name: string = "light_01_2"
            }
            0xc9bba569 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.58853686
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    893.746094, 189.977539, 1412.72656, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_SpaceTrees"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_SpaceTrees" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xcb99e29d = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1983.81787, -0.000122070312, 1960.07886, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop1"
            }
            0xf7d6f945 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Fountain_Water"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3303.29907, 4.04733276, 1504.25244, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Fountain_Water1"
            }
            0xf9a4e6d0 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Birds"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.65332, 162.745728, 1922.89124, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Birds1"
            }
            0xdd6a0666 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tree_Branches"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1828.43958, -6.10351562e-05, 1765.69434, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Tree_Branches1"
            }
            0x61769394 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Tones_Meditation"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2027.39282, 67.2710876, 1985.72168, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Tones_Meditation1"
            }
            0xb3666176 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Chimes_Clang"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.25293, 77.2751465, 1989.10058, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Chimes_Clang1"
            }
            0x7fd1b6f2 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/SpaceTrees/TFT_Audio-Emitter_Galaxy_SpaceTrees_Crickets"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1891.01733, 166.192627, 1921.85742, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_SpaceTrees_Crickets1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_SpaceTrees"
    }
    0x4ddca076 = MapPointLightType {
        radius: f32 = 800
        Impact: i32 = 1
    }
    0x52248cce = MapPointLightType {
        lightColor: vec4 = { 0.690196097, 0.227450982, 0.772549033, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x7ca5e4f1 = MapPointLightType {
        lightColor: vec4 = { 0.105882354, 0.321568638, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xf232d9bd = MapPointLightType {
        lightColor: vec4 = { 0.749019623, 0.549019635, 0.443137258, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x55ee3022 = MapPointLightType {
        lightColor: vec4 = { 0.70588237, 0.498039216, 0.0745098069, 1 }
        radius: f32 = 700
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x72e7702e = MapPointLightType {
        lightColor: vec4 = { 1, 0.75686276, 0.545098066, 1 }
        radius: f32 = 6000
        Impact: i32 = 1
    }
    0xdc31003a = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.717647076, 0.823529422, 1 }
    }
    0xdd24adc9 = MapPointLightType {
        lightColor: vec4 = { 0.525490224, 0.509803951, 0.466666669, 1 }
    }
}
