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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_LandingSite_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_LandingSite_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Board_LandingSite_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Models/Monitor_Large_A/Materials/ENV_TileableDiffuse_SolarPanel_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Monitor_Large_A/Materials/ENV_TileableDiffuse_SolarPanel_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/SolarPanel_Tileable_A.TFT_ArenaSkin_Galaxy1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "UV_TileAmount"
                value: vec4 = { 4, 2, 0, 0 }
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Glass_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Glass_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "FlowMap"
                textureName: string = "ASSETS/Maps/Particles/Odyssey/OD_Waterfall_Flowmap.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Emission_X_Noise_Mask"
                textureName: string = "ASSETS/Maps/Particles/Odyssey/OD_Waterfall_NoiseMask.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/Particles/Odyssey/OD_color-darksmoke.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_UV_Tiling"
                value: vec4 = { 1, 0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MaxFlowStrength"
                value: vec4 = { 0.472499996, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flow_Speed"
                value: vec4 = { 0.605000019, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flow_Distance"
                value: vec4 = { 0.485000014, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Strength"
                value: vec4 = { 0.242500007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Strength"
                value: vec4 = { 0.600000024, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { 0.34117648, 0.529411793, 0.647058845, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_UVScale"
                value: vec4 = { 1, 0.701960802, 0.00784313772, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emmissive_Intensity"
                value: vec4 = { 1.14999998, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { 0, -0.200000003, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Scale"
                value: vec4 = { 0.800000012, 0.699999988, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "EMMISSIVE_WorldSpace_GradientBounds_MIN_MAX"
                value: vec4 = { 0, 50, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rim_Color"
                value: vec4 = { 0.431372553, 0.925490201, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rim_Intensity"
                value: vec4 = { 2.5875001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rim_Power"
                value: vec4 = { 2.36249995, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Specular_Color"
                value: vec4 = { 0.521568656, 1, 0.200000003, 0.501960814 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Emission_Anim_Frequency"
                value: vec4 = { 2.70000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emission_Anim_Amplitude"
                value: vec4 = { 0.115000002, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emission_Anim_Offset"
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_UV_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_FLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "EMISSIVE_IS_TEXTURE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "EMISSIVE_GRADIENT_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_RIM_LIGHT"
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_EMMISSIVE_MASTER"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_FLOW_ALPHA_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_UV_ALPHA_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_EMISSION_TEXTURE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ANIMATED_EMISSION"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_EMISSIVE_SCROLL"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/OD_FlowMap"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Emissive_Color"
                    enabled: bool = false
                    driver: pointer = ColorGraphMaterialDriver {
                        driver: pointer = SineMaterialDriver {
                            mDriver: pointer = TimeMaterialDriver {}
                        }
                        colors: embed = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec4] = {
                                { 1, 0.717647076, 0, 1 }
                                { 0.819607854, 1, 0, 1 }
                            }
                        }
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Pipes_Modular_Malphite_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Pipes_Modular_Malphite_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Pipes_Modular_Malphite_A.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_A.TFT_ArenaSkin_Odyssey_Polish.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Stripes_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Stripes_B.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Clean_A.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Skybox_Landingsite_A" = VfxSystemDefinitionData {
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
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_Landingsite_A"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Skybox_Landingsite_A"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Electricity_Hum" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Electricity_Hum"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Electricity_Hum"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_landingsite_electricity_hum"
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/Galaxy_Blackhole_Wind" = VfxSystemDefinitionData {
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
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/Galaxy_Blackhole_Wind"
        flags: u8 = 197
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Satellite_Beeps" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Satellite_Beeps"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Satellite_Beeps"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_landingsite_satellite_beeps"
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Pump" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Pump"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Pump"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_landingsite_jet_pump"
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Beeps" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Beeps"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Beeps"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_landingsite_jet_beeps"
    }
    "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Radio" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Radio"
        particlePath: string = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Radio"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_landingsite_jet_radio"
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
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x81b96d1c = null
            0x1b889fbf = null
            0xfb4e4285 = null
            0x1d2f3886 = null
            0xd34d746a = null
            0xacf38460 = null
            0x69c17485 = null
            0xc0bfe294 = null
            0x0f79408e = null
            0xeb460297 = null
            0x5f4edc70 = null
            0x02782484 = null
            0x64bb974e = null
            0xee0b6ce8 = null
            0x82e5d193 = null
            0x13589c9b = null
            0xc0fe9d96 = null
            0x942d64a2 = null
            0x04e901ec = null
            0xff02dc46 = null
            0xd4739083 = null
            0x01f0bc19 = null
            0x2001470a = null
            0xb23fb7d9 = null
            0x70669634 = null
            0xb849e2de = null
            0xf6f2dd4e = null
            0xcf899bcb = null
            0x7c777510 = null
            0xc91fcca3 = null
            0x44183ec8 = null
            0x85c1aa1a = null
            0x8eccfd10 = null
            0x846c610f = null
            0x6e5c4e4e = null
            0xab2980c6 = null
            0x57dc655d = null
            0x065ac233 = null
            0x12dcfc8e = null
            0x0ce2d294 = null
            0xf626d8c9 = null
            0x238489bc = null
            0xce8c62b4 = null
            0xacb0e5ec = null
            0x1668cffe = null
            0xf0423007 = MapGroup {
                members: list2[string] = {
                    "5ebf5406-4b05-45bc-8a5a-478313b75950"
                    "a0cb672a-a0f1-4c23-a720-a33f3eaa23e8"
                    "ae7eb4a1-29d5-4701-8fea-923cddf5fe0b"
                    "bfb0cf39-e924-43a7-ae8f-639200a3f6a6"
                    "546cbf4e-cf9b-4460-b6ee-0113c343e62a"
                    "91115c23-0703-458a-81df-971087067cab"
                    "fe223944-736f-40d5-b406-ff07f7bced75"
                }
                transform: mtx44 = {
                    -0.707107306, 0, -0.707106948, 0
                    0, 1, 0, 0
                    0.707106948, 0, -0.707107306, 0
                    3170.2522, 10.2225113, 1845.73669, 1
                }
                name: string = "group2"
            }
            0xdda0f429 = null
            0xe02115a1 = null
            0xdafd551b = null
            0x7fd0dc97 = null
            0x78792126 = null
            0x9cc4cdcc = null
            0x76daa842 = null
            0x84d00edf = null
            0x0f0e45c1 = MapGroup {
                members: list2[string] = {
                    "5bee89d4-d0dc-4404-bcce-d0067094f4c0"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3136.81885, 1.01534653, 1881.00159, 1
                }
                name: string = "group3"
            }
            0x31cb70ab = MapGroup {
                members: list2[string] = {
                    "ae7eb4a1-29d5-4701-8fea-923cddf5fe0b"
                    "a0cb672a-a0f1-4c23-a720-a33f3eaa23e8"
                    "546cbf4e-cf9b-4460-b6ee-0113c343e62a"
                    "5ebf5406-4b05-45bc-8a5a-478313b75950"
                    "bfb0cf39-e924-43a7-ae8f-639200a3f6a6"
                    "91115c23-0703-458a-81df-971087067cab"
                }
                transform: mtx44 = {
                    0.707106709, 0, -0.707106829, 0
                    0, 1, 0, 0
                    0.707106829, 0, 0.707106709, 0
                    3172.98779, 10.3526516, 1824.35815, 1
                }
                name: string = "group4"
            }
            0x7e19e8a7 = null
            0x9e15d788 = null
            0x6bfe6513 = null
            0x907e3ac9 = null
            0xd05ee2ce = null
            0x7187fbfb = null
            0x074e1f90 = null
            0xde4d07d1 = null
            0x00b3b1ee = null
            0xcc947d1e = null
            0x18dda326 = null
            0x1d59dc6a = null
            0x8db1a935 = null
            0x69ae80b4 = null
            0x1652e364 = null
            0xde5dbf72 = null
            0x5bb0e645 = null
            0x90e813e5 = null
            0xd8c92bc8 = null
            0x28ef1390 = null
            0x26cbb8de = null
            0x1d266f1f = null
            0xafe72bc0 = null
            0x22752fb8 = null
            0x20cab251 = null
            0xcb4c5b74 = null
            0xeb1b4887 = null
            0xa3986aba = null
            0x0ae104a1 = null
            0x4d2d0444 = MapGroup {
                members: list2[string] = {
                    "b3364948-8b5e-40e0-9693-8df8650f3ff5"
                }
                transform: mtx44 = {
                    -1.71575351e-07, 0, -1.43927824, 0
                    0, 1.43927836, 0, 0
                    0.826441348, 0, -9.8519493e-08, 0
                    260.980347, -6.61133528, 2667.146, 1
                }
                name: string = "group6"
            }
            0x8359cc7d = MapGroup {
                members: list2[string] = {
                    "1437ea7a-9ddf-46cd-9712-02d49066218c"
                }
                transform: mtx44 = {
                    -1.71575351e-07, 0, -1.43927824, 0
                    0, 1.43927836, 0, 0
                    0.826441348, 0, -9.8519493e-08, 0
                    260.980347, -6.61133528, 2869.24243, 1
                }
                name: string = "group7"
            }
            0x1010ae46 = null
            0xf486723b = null
            0xaf732bf0 = MapGroup {
                members: list2[string] = {
                    "213631db-61db-4fc1-b8d0-77baf8f37ca3"
                }
                transform: mtx44 = {
                    -1.45398784, 0, -1.17587209, 0
                    0, 1.85224342, 0, 0
                    0.713411868, 0, -0.882147133, 0
                    369.333679, -28.6956997, 3055.8916, 1
                }
                name: string = "group8"
            }
            0x8a009376 = null
            0xf0d17ebc = null
            0xf35eb277 = MapGroup {
                members: list2[string] = {
                    "f2dcf620-17bb-408d-81fc-e2e47f3b9d47"
                    "5376f2c0-ca91-4fbc-ab04-b0049c520a71"
                }
                transform: mtx44 = {
                    -1.43927813, 0, 3.43150674e-07, 0
                    0, 1.43927836, 0, 0
                    -2.21669666e-07, 0, -0.929749846, 0
                    662.649231, -6.61133528, 3307.43408, 1
                }
                name: string = "group9"
            }
            0x2f2becec = null
            0x1a40f85f = null
            0x41191c63 = MapGroup {
                members: list2[string] = {
                    "83bd87d5-91f8-47f2-a737-f6a292f12b42"
                }
                transform: mtx44 = {
                    -1.43927813, 0, 3.43150674e-07, 0
                    0, 1.43927836, 0, 0
                    -2.21669666e-07, 0, -0.929749846, 0
                    864.52417, -6.61133528, 3307.43408, 1
                }
                name: string = "group10"
            }
            0x3e4c9bac = null
            0xff4e8382 = null
            0x96d3aedf = MapGroup {
                members: list2[string] = {
                    "92fcd386-b6bd-43a5-aa82-c7f96ca70915"
                }
                transform: mtx44 = {
                    -0.575026929, 0, -1.107342, 0
                    0, 1.43927836, 0, 0
                    0.79812938, 0, -0.414457291, 0
                    517.968994, -6.61133528, 3223.89062, 1
                }
                name: string = "group11"
            }
            0xe18da156 = null
            0x22254bfe = null
            0xd48b311d = null
            0x16a5549c = null
            0xa53ca4af = MapGroup {
                members: list2[string] = {
                    "9c56d771-fa1b-43ae-bbfc-e71920ab5fc8"
                    "4c58b642-c730-4886-a0f2-8a79119f783f"
                }
                transform: mtx44 = {
                    0.999078631, 0, -0.0429172292, 0
                    0, 1, 0, 0
                    0.0505778603, 0, 1.17741191, 0
                    1014.13806, -340.433716, 1411.57288, 1
                }
                name: string = "group12"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_LandingSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xfa5734b8 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/Galaxy_Blackhole_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1826.55151, 158.593597, 1699.44568, 1
                }
                name: string = "Galaxy_Blackhole_Wind1"
            }
            0xea4ae8bb = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/Galaxy_Blackhole_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2502.6394, 158.593475, 2424.47925, 1
                }
                name: string = "Galaxy_Blackhole_Wind2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_LandingSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_LandingSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xcc2b69c8 = MapLightingVolume {
                sunColor: vec4 = { 0.423529416, 0.588235319, 0.647058845, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                0xba02f116: f32 = 0.100000001
                skyLightColor: vec4 = { 0.427450985, 0.56078434, 0.607843161, 1 }
                horizonColor: vec4 = { 0.301960796, 0.329411775, 0.482352942, 1 }
                groundColor: vec4 = { 0.152941182, 0.156862751, 0.247058824, 1 }
                skyLightScale: f32 = 0.600000024
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.0666666701, 0.0666666701, 0.137254909, 1 }
                fogAlternateColor: vec4 = { 0.20784314, 0.152941182, 0.31764707, 1 }
                fogStartAndEnd: vec2 = { 250, -600 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2186.59424, -927.355957, 2144.35596, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_LandingSite"
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
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_LandingSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xb3a80e32 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1979.89966, -62.0596619, 1873.02783, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop1"
            }
            0x3516da2c = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Radio"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1254.14905, 434.148743, 2643.9021, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Radio1"
            }
            0xb54a02ba = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Satellite_Beeps"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2675.91724, 23.3878021, 1859.98999, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Satellite_Beeps1"
            }
            0x91070a1c = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Electricity_Hum"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2113.90576, 163.150543, 1425.15161, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Electricity_Hum1"
            }
            0x60418ff9 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Beeps"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1295.13708, 30.6309814, 1937.70532, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Beeps1"
            }
            0x776a4f04 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Pump"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2970.17676, 108.769653, 2193.66553, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_LandingSite_Jet_Pump1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_LandingSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_LandingSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa77a97fd = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    842.518311, -388.330383, 813.353394, 1
                }
                name: string = "Freljord_FG_Torch7"
            }
            0x02515464 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.939920366
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1850.64136, -388.330383, 3521.35474, 1
                }
                name: string = "Freljord_FG_Torch8"
            }
            0x8a6189db = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3074.9541, -441.034424, 1258.29236, 1
                }
                name: string = "Freljord_FG_Torch9"
            }
            0xc0de16cf = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2506.0957, 804.190735, 115.258636, 1
                }
                name: string = "Light_Point_Center_DragonCloud13"
            }
            0xebd62717 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3401.30615, -388.330383, 2370.31909, 1
                }
                name: string = "Freljord_FG_Torch10"
            }
            0x19bb1465 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2198.21289, -388.330383, 779.626587, 1
                }
                name: string = "Freljord_FG_Torch12"
            }
            0xcbca7a32 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    555.900269, -388.330383, 1879.703, 1
                }
                name: string = "Freljord_FG_Torch1"
            }
            0x858c7197 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3407.65308, -156.109467, 2372.32715, 1
                }
                name: string = "Freljord_WC_Blue_Fill1"
            }
            0x10e25c66 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3278.25903, -156.109467, 1512.8844, 1
                }
                name: string = "Freljord_WC_Blue_Fill2"
            }
            0x2a518982 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2868.2334, 18.1271057, 803.102661, 1
                }
                name: string = "Freljord_WC_Blue_Fill3"
            }
            0xdde3e32b = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2237.0415, -156.109467, 783.271912, 1
                }
                name: string = "Freljord_WC_Blue_Fill4"
            }
            0x7bd2f286 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    856.657104, -156.109467, 783.271912, 1
                }
                name: string = "Freljord_WC_Blue_Fill5"
            }
            0x5000ea44 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    576.649841, -156.109467, 1874.81702, 1
                }
                name: string = "Freljord_WC_Blue_Fill6"
            }
            0x94ec6f57 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1886.20361, -156.109467, 3517.76025, 1
                }
                name: string = "Freljord_WC_Blue_Fill7"
            }
            0xb470a77d = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.632052302
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3246.04663, -156.109467, 3302.24902, 1
                }
                name: string = "Freljord_WC_Blue_Fill8"
            }
            0xe23349fe = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.939920306
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3210.48438, -388.330383, 3305.84351, 1
                }
                name: string = "Freljord_FG_Torch2"
            }
            0xe52d3d97 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.801788688
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    265.200989, 244.494263, 3500.21265, 1
                }
                name: string = "Freljord_WC_Blue_Fill9"
            }
            0x10d7b6cd = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    248.298065, 747.077698, 2668.62939, 1
                }
                name: string = "Freljord_FG_Torch3"
            }
            0xfe2be577 = MapPointLight {
                type: link = 0x553c4952
                radiusScale: f32 = 1.00150788
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1133.151, 372.003204, 1436.75, 1
                }
                name: string = "Light_Point_Brazier_DragonCloud1"
            }
            0xd85f5349 = MapPointLight {
                type: link = 0x553c4952
                radiusScale: f32 = 1.00150716
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2863.67993, 364.212677, 2649.23511, 1
                }
                name: string = "Light_Point_Brazier_DragonCloud2"
            }
            0x49a9e698 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.23467159
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    973.829468, 219.719421, 2348.78101, 1
                }
                name: string = "Light_Red_01_1"
            }
            0x3f272b09 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.34761882
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1200.07666, 219.719421, 2940.67285, 1
                }
                name: string = "Light_Red_01_2"
            }
            0x1eae6e33 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.70760608
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    157.02652, 339.757172, 1986.79565, 1
                }
                name: string = "Light_Red_01_3"
            }
            0xc36eb08e = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.70760608
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3630.45483, 339.757172, 1986.79565, 1
                }
                name: string = "Light_Red_01_4"
            }
            0x6ff19e0f = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.70760596
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2106.27075, 339.757172, 3622.02319, 1
                }
                name: string = "Light_Red_01_5"
            }
            0x4411ecc8 = MapPointLight {
                type: link = 0x534460ea
                radiusScale: f32 = 1.70760608
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2106.27075, 339.757172, 624.033691, 1
                }
                name: string = "Light_Red_01_6"
            }
            0xa16059e5 = MapPointLight {
                type: link = 0x45dda18a
                radiusScale: f32 = 1.18141556
                intensityScale: f32 = 1.64999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1989.89697, 486.53125, 2044.33398, 1
                }
                name: string = "Light_Green_01_1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_LandingSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite_Skybox" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa588fd89 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/LandingSite/TFT_Skybox_Landingsite_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1974.53247, 0, 2060.22266, 1
                }
                name: string = "TFT_Skybox_Landingsite_A1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite_Skybox"
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
    "Maps/MapGeometry/Map22/Galaxy_LandingSite" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Galaxy_LandingSite"
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
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Galaxy_LandingSite/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Galaxy_LandingSite_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            "Galaxy_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base"
            0x32425435 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared"
            0x5165e3f8 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite"
            0x01bc2f23 = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_LandingSite"
            0x16309bc5 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_LandingSite"
            0x2d2f1443 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_LandingSite"
            0xc39040ad = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_LandingSite"
            0x6bb22423 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_LandingSite_Skybox"
        }
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
    0x7ca5e4f1 = MapPointLightType {
        lightColor: vec4 = { 0.105882354, 0.321568638, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x534460ea = MapPointLightType {
        lightColor: vec4 = { 0.866666675, 0.80392158, 0.443137258, 1 }
        specular: bool = false
        Impact: i32 = 1
    }
}
