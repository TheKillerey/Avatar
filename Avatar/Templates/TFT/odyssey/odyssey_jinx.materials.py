#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Odyssey/Models/Board_A/Materials/Board_A_Light_Sequence_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Board_A/Materials/Board_A_Light_Sequence_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Board_A.TFT_ArenaSkin_Odyssey_Polish.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Board_A_Mask.TFT_ArenaSkin_Odyssey.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "ColorDodge_Amount"
                value: vec4 = { 0.412499994, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Loop_Reset_Duration"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Start_Delay"
                value: vec4 = { 7.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "End_Delay"
                value: vec4 = { 1.20000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fade_Time"
                value: vec4 = { 3.2750001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_FADE_OUT"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Light_Sequence"
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
    "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Lights_A/Materials/Hangar_Lights_A_Light_Sequence_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Lights_A/Materials/Hangar_Lights_A_Light_Sequence_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_A.TFT_ArenaSkin_Galaxy2.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Hangar_Lights_Mask_A.TFT_ArenaSkin_Odyssey.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "ColorDodge_Amount"
                value: vec4 = { 0.952499986, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Loop_Reset_Duration"
                value: vec4 = { 4.67500019, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Start_Delay"
                value: vec4 = { 3.375, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "End_Delay"
                value: vec4 = { 0.125, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fade_Time"
                value: vec4 = { 0.75, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 3, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_FADE_OUT"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Light_Sequence"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Jinx/Materials/ENV_TileableDiffuse_Hangar_Tile_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Jinx/Materials/ENV_TileableDiffuse_Hangar_Tile_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Metal_Panels_Tileable_A.TFT_ArenaSkin_Galaxy2.dds"
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
                value: vec4 = { 0.521568656, 0.470588237, 0.631372571, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Softness"
                value: vec4 = { 1075.00073, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Offset"
                value: vec4 = { 1.05999994, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_OBJECT_GRADIENT"
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
    "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Jinx/Materials/ENV_TileableDiffuse_Hangar_Trim_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Models/Hangar_Jinx/Materials/ENV_TileableDiffuse_Hangar_Trim_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_A.TFT_ArenaSkin_Galaxy2.dds"
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
                value: vec4 = { 0.458823532, 0.384313732, 0.607843161, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Softness"
                value: vec4 = { 1075, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Gradient_Offset"
                value: vec4 = { 1.34000003, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_OBJECT_GRADIENT"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Jinx_Decals_MAT_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Jinx_Decals_MAT_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Jinx_Decals_A.TFT_ArenaSkin_Odyssey.dds"
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
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/BulletShell_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/BulletShell_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Odyssey_BullletShell_A.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jinx_Props_MAT_B" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jinx_Props_MAT_B"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jinx_Props.TFT_ArenaSkin_Odyssey_Polish.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jinx_Props_MAT_A" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jinx_Props_MAT_A"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jinx_Props.TFT_ArenaSkin_Odyssey_Polish.dds"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
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
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Space_Mist" = VfxSystemDefinitionData {
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
                    constantValue: vec4 = { 0.560006082, 0.930006862, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.105412915, 0.868006408, 1, 0 }
                            { 0.0746674836, 0.919065595, 1, 0.300007641 }
                            { 0.0329415351, 0.521533251, 1, 0.300007641 }
                            { 0.116393425, 0.240707666, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
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
                miscRenderFlags: u8 = 1
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
                    constantValue: vec4 = { 0.647058845, 0.984313726, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.647058845, 0.984313726, 1, 0 }
                            { 0.647058845, 0.984313726, 1, 1 }
                            { 0.157324106, 0.563567877, 1, 1 }
                            { 0.170011535, 0.293364078, 1, 0 }
                        }
                    }
                }
                pass: i16 = -10
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
                            { 1, 0.466666669, 0.200000003, 0.500007629 }
                            { 1, 0, 0.482352942, 0.22549364 }
                            { 0, 0.650980413, 1, 0 }
                        }
                    }
                }
                pass: i16 = -6
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
        particleName: string = "TFT_Odyssey_Jinx_Space_Mist"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Space_Mist"
        soundOnCreateDefault: string = "Play_sfx_tft_env_darkstar_common_fire"
        flags: u8 = 212
        buildUpTime: f32 = 5
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale3" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
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
                emitterName: string = "lightEmitterBig"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh_Scale3.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100007631 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.737254918, 0.521568656, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.659192622, 0.182037681, 0 }
                            { 1, 0.505959272, 0.075678587, 1 }
                            { 1, 0.396093816, 0.220899656, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "lightEmitterSmall"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh_Scale3.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.894117653, 0.349019617, 0 }
                            { 1, 0.686274529, 0.145098045, 1 }
                            { 1, 0.53725493, 0.423529416, 0 }
                        }
                    }
                }
                pass: i16 = 1
                depthBiasFactors: vec2 = { -1, -5 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_LightString_Scale3"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale3"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
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
                emitterName: string = "lightEmitterBig"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh_Scale2.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100007631 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.737254918, 0.521568656, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.659192622, 0.182037681, 0 }
                            { 1, 0.505959272, 0.075678587, 1 }
                            { 1, 0.396093816, 0.220899656, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "lightEmitterSmall"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh_Scale2.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.894117653, 0.349019617, 0 }
                            { 1, 0.686274529, 0.145098045, 1 }
                            { 1, 0.53725493, 0.423529416, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -5 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_LightString_Scale2"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale2"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Light_Flare" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                importance: u8 = 2
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
                    constantValue: vec4 = { 1, 0.859998465, 0.540001512, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.859998465, 0.540001512, 0 }
                            { 1, 0.859998465, 0.540001512, 0.800000012 }
                            { 1, 0.859998465, 0.540001512, 0 }
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
        }
        particleName: string = "TFT_Odyssey_Jinx_Light_Flare"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Light_Flare"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_ShipLightFog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                    constantValue: vec4 = { 0, 0.820004582, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.820004582, 1, 0 }
                            { 0, 0.820004582, 1, 0.400000006 }
                            { 0, 0.820004582, 1, 0 }
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
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 800, 300, 50 }
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
                            { 800, 300, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Slash_Flare.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_ShipLightFog"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_ShipLightFog"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.123000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.123000003
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks_Child"
                        }
                    }
                }
                emitterName: string = "Basic"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 150 }
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
                                { 80, 0, 150 }
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
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0 }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 45 }
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
                            { 45, 0, 45 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/disc32.TFT_Set4.DDS"
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_Sparks"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
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
                emitterName: string = "lightEmitterBig"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100007631 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.737254918, 0.521568656, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.659192622, 0.182037681, 0 }
                            { 1, 0.505959272, 0.075678587, 1 }
                            { 1, 0.396093816, 0.220899656, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -4 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "lightEmitterSmall"
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
                emissionMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Jinx_LightString_EmitMesh.TFT_ArenaSkin_Odyssey.scb"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.894117653, 0.349019617, 0 }
                            { 1, 0.686274529, 0.145098045, 1 }
                            { 1, 0.53725493, 0.423529416, 0 }
                        }
                    }
                }
                pass: i16 = 1
                depthBiasFactors: vec2 = { -1, -5 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Item_StatikkShiv_Orange_Glow.TFT_Set4.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_LightString"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Station_Amb" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Odyssey_Jinx_Station_Amb"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Station_Amb"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_jinx_station_amb"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Amb2D" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Odyssey_Jinx_Amb2D"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Amb2D"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_jinx_amb2D"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Jets" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
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
                    constantValue: vec3 = { 100, 1000, 0 }
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
                            { 100, 1000, 0 }
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
                        constantValue: vec3 = { 40, 0, 40 }
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
                            { 0, 0.517647088, 1, 1 }
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
                            { 0.580392182, 0.866666675, 1, 0 }
                            { 0.294117659, 0.423529416, 1, 1 }
                            { 0.152941182, 0.13333334, 0.709803939, 0 }
                        }
                    }
                }
                pass: i16 = -2
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
                    constantValue: vec3 = { 0.600000024, 7, 0.600000024 }
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
                emitterName: string = "flameCylinder"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
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
                            { 0, 400, 0 }
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
                    constantValue: vec4 = { 0.220004573, 1, 0.949996173, 0.800000012 }
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
                            { 0.220004573, 1, 0.949996173, 0.800000012 }
                        }
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
                            { 0, 0.615686297, 1, 1 }
                            { 0, 0.450980395, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
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
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Shared/Particles/alphaslice_mesh.ARAM_VFX_Update.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 0.899999976, 7, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.39999998
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.39999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.899999976, 7, 0.899999976 }
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
                            { 1, 0.5, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_WispTrail_Add.ARAM_VFX_Update.dds"
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
                            { 1, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 2, 1 }
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
                    constantValue: vec3 = { 0, 600, 0 }
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
                            { 0, 600, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                shape: embed = VfxShape {
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
                    constantValue: vec4 = { 0, 0.568627477, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.568627477, 1, 0 }
                            { 0, 0.568627477, 1, 1 }
                            { 0, 0.0847366378, 1, 1 }
                            { 0, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 51
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
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
                depthBiasFactors: vec2 = { -1, -8 }
                miscRenderFlags: u8 = 1
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
                    constantValue: vec3 = { 150, 1, 0 }
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
                            { 150, 1, 0 }
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
                                    0.800000012
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
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
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
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 200, 50 }
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
                            { 600, 200, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Slash_Flare.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/Flame_trail_gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 10
                }
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_Jets"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Jets"
        soundPersistentDefault: string = "Play_sfx_tft_env_odyssey_common_jet_thrusters"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start_Away" = VfxSystemDefinitionData {
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
                            { 1, 0.36470589, 0.670588255, 0 }
                            { 1, 0.454901963, 0.97647059, 1 }
                            { 0.619607866, 0.345098048, 0.709803939, 0 }
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
                            { 0.572549045, 0.850980401, 1, 0 }
                            { 0.321568638, 0.53725493, 1, 1 }
                            { 0.145098045, 0.278431386, 0.709803939, 0 }
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
                            { 0.454901963, 0.145098045, 0.709803939, 0 }
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
                    paletteCount: i32 = 3
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
                    constantValue: vec4 = { 0.435294122, 0.172549024, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.435294122, 0.172549024, 1, 0 }
                            { 0.435294122, 0.172549024, 1, 0.800000012 }
                            { 0.435294122, 0.172549024, 1, 0 }
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
                    constantValue: vec4 = { 0.352941185, 0.43921569, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.352941185, 0.43921569, 1, 0 }
                            { 0.352941185, 0.43921569, 1, 0.800000012 }
                            { 0.352941185, 0.43921569, 1, 0 }
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
        particleName: string = "TFT_GoldMine_Odyssey_Jinx_Start_Away"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start_Away"
        flags: u8 = 199
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
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.29999995
                }
                emitterName: string = "Aura_"
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
        particleName: string = "TFT_Odyssey_Jinx_Arena_JetThruster01"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster01"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster02" = VfxSystemDefinitionData {
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
                            { 1, 1, 1, 1 }
                            { 1, 0.764705896, 0.164705887, 1 }
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
                    constantValue: vec3 = { 9.75, 25, 25 }
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
                    constantValue: vec3 = { 800, 500, 500 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/ShieldRing.dds"
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
                    constantValue: vec4 = { 0.513725519, 0.470588237, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.513725519, 0.470588237, 1, 0 }
                            { 0.513725519, 0.470588237, 1, 1 }
                            { 0.513725519, 0.470588237, 1, 0 }
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
                    constantValue: vec3 = { 6, 5, 6 }
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
                    constantValue: vec3 = { 6, 2, 6 }
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
                    constantValue: vec3 = { 6, 3, 6 }
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 5, 3 }
                }
                texture: string = "ASSETS/Shared/Particles/Base_DottedGrid.TFT_ArenaSkin_Odyssey.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.125, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.64999998, 1 }
                }
                textureMult: string = "ASSETS/Shared/Particles/Z_GradientV.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
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
                    constantValue: f32 = 0.529999971
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
                        constantValue: vec3 = { 0, 325, 0 }
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
                                { 0, 325, 0 }
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
                    constantValue: vec4 = { 0.431372553, 0.725490212, 1, 0.792156875 }
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
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
                            { 0.431372553, 0.725490212, 1, 0 }
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
                            { 0.431372553, 0.725490212, 1, 0.792156875 }
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
                    constantValue: vec3 = { 275, 750, 275 }
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
                            { 275, 750, 275 }
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
                    constantValue: f32 = 0.340000004
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
                        constantValue: vec3 = { 0, 375, 0 }
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
                                { 0, 375, 0 }
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
                    constantValue: vec3 = { 275, 750, 275 }
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
                            { 275, 750, 275 }
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
                    constantValue: f32 = 0.720000029
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
                                { 0, 500, 0 }
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
                    constantValue: vec4 = { 0.423529416, 0.627451003, 1, 0.792156875 }
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
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
                            { 0.423529416, 0.627451003, 1, 0 }
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
                            { 0.423529416, 0.627451003, 1, 0.792156875 }
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
                    constantValue: vec3 = { 275, 750, 275 }
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
                            { 275, 750, 275 }
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
                    constantValue: f32 = 3
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
                                    0.75
                                    1.25
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
                    12
                }
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.329411775, 0.631372571, 1, 0.360784322 }
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
                    deltaIn: f32 = 350
                }
                depthBiasFactors: vec2 = { 1, 6 }
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
                                    1.20000005
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 450, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 0.549996197, 1, 0.650003791 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.269993126, 0.549996197, 1, 0 }
                            { 0.269993126, 0.549996197, 1, 0.650003791 }
                            { 0.269993126, 0.549996197, 1, 0.650003791 }
                            { 0.269993126, 0.549996197, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                alphaRef: u8 = 25
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1200, 50 }
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
                emitterName: string = "Gold1"
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
                                    1.20000005
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 650, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 0.549996197, 1, 0.250003815 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.269993126, 0.549996197, 1, 0 }
                            { 0.269993126, 0.549996197, 1, 0.250003815 }
                            { 0.269993126, 0.549996197, 1, 0.250003815 }
                            { 0.269993126, 0.549996197, 1, 0 }
                        }
                    }
                }
                pass: i16 = 500
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1200, 50 }
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
        particleName: string = "TFT_Odyssey_Jinx_Arena_JetThruster02"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster02"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start" = VfxSystemDefinitionData {
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
                            { 1, 0.36470589, 0.670588255, 0 }
                            { 1, 0.454901963, 0.97647059, 1 }
                            { 0.619607866, 0.345098048, 0.709803939, 0 }
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
                            { 0.572549045, 0.850980401, 1, 0 }
                            { 0.321568638, 0.53725493, 1, 1 }
                            { 0.145098045, 0.278431386, 0.709803939, 0 }
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
                            { 0.454901963, 0.145098045, 0.709803939, 0 }
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
                    paletteCount: i32 = 3
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
                    constantValue: vec4 = { 0.435294122, 0.172549024, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.435294122, 0.172549024, 1, 0 }
                            { 0.435294122, 0.172549024, 1, 0.800000012 }
                            { 0.435294122, 0.172549024, 1, 0 }
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
                    constantValue: vec4 = { 0.352941185, 0.43921569, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.352941185, 0.43921569, 1, 0 }
                            { 0.352941185, 0.43921569, 1, 0.800000012 }
                            { 0.352941185, 0.43921569, 1, 0 }
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
        particleName: string = "TFT_GoldMine_Odyssey_Jinx_Start"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start"
        flags: u8 = 199
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    15
                }
                isSingleParticle: flag = true
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2500, 0 }
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
                            { 0, 2500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 3, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -800, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
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
                                            30
                                            -30
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
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.811764717, 0.482352942, 1 }
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
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.649999976
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
                            0.100000001
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.811764717, 0.482352942, 0 }
                            { 1, 0.811764717, 0.482352942, 1 }
                            { 1, 0.811764717, 0.482352942, 1 }
                            { 1, 0.811764717, 0.482352942, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
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
                                    800
                                    -800
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
                directionVelocityScale: f32 = 0.00300000003
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Kayn_Skin02_Sparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
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
                    12
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "jjFlare"
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
                    constantValue: vec4 = { 1, 0.75686276, 0.13333334, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.75686276, 0.13333334, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 20, 50 }
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
                            { 30, 20, 50 }
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
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Dmg_Skin04_Tar_Glow_02.TFT_Set3.dds"
            }
        }
        particleName: string = "TFT_Odyssey_Jinx_Sparks_Child"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks_Child"
        soundOnCreateDefault: string = "Play_sfx_tft_env_odyssey_common_electricity_sparking"
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Hangar_Volume" = VfxSystemDefinitionData {
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.770000756, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.770000756, 1, 0 }
                            { 0, 0.770000756, 1, 0.800000012 }
                            { 0, 0.770000756, 1, 0 }
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
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Odyssey_Jinx_Hangar_Volume"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Hangar_Volume"
        buildUpTime: f32 = 4
    }
    "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Jet_Thrusters" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Odyssey_Jinx_Jet_Thrusters"
        particlePath: string = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Jet_Thrusters"
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
    "Maps/Particles/TFT/Odyssey/TFT_Skybox_Odyssey_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "FloatingRock01"
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
                    constantValue: vec4 = { 0.819607854, 0.635294139, 0.796078444, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.827450991, 0.984313726, 1 }
                }
                pass: i16 = -47
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
                    constantValue: vec2 = { -0.00100000005, 0 }
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
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_RockLayer.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.501960814, 0.717647076, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.796078444, 0.937254906, 1 }
                }
                pass: i16 = -45
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
                pass: i16 = -50
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
                    constantValue: vec4 = { 0.639993906, 0.639993906, 1, 0.250003815 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.469993144, 0.429999232, 0.62999922, 0.209994659 }
                }
                pass: i16 = 5
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
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PurpleCloud01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 3 }
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
                    constantValue: vec4 = { 1, 1, 1, 0.269993126 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.889997721, 0.510002315 }
                }
                pass: i16 = 3
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PurpleCloud01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 3 }
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
                pass: i16 = -49
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.300000012, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_StarsC.dds"
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
                emitterName: string = "Light Belt01"
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
                    constantValue: vec4 = { 0.650003791, 0.229999244, 0.639993906, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.579995394, 1, 0.489997715 }
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
                emitterName: string = "Light Belt02"
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
                    constantValue: vec4 = { 0.843137264, 0.580392182, 0.639215708, 0.56078434 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.717647076, 1, 0.541176498, 0.31764707 }
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
                emitterName: string = "Cloud Noise"
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
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_CloudNoise.TFT_ArenaSkin_Odyssey.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.250003815, 0.409994662, 0.590005338 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.179995418, 0.960006118, 0.379995435 }
                }
                pass: i16 = 13
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.300000012, 0.300000012 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_CloudyNoise01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0399999991, 0 }
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
                        constantValue: vec3 = { 0, 70, 0 }
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
                    constantValue: vec4 = { 1, 0.733333349, 0.945098042, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.858823538, 0.666666687, 0.713725507, 1 }
                }
                pass: i16 = -46
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
                emitterName: string = "PlanetA"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 60, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Odyssey/TFT_Odyssey_Skybox_PlanetA.TFT_ArenaSkin_Odyssey_Polish.scb"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = -48
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.219999999, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_PlanetA.dds"
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_Odyssey_A"
        particlePath: string = "Maps/Particles/TFT/Odyssey/TFT_Skybox_Odyssey_A"
        flags: u8 = 197
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
    "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xfa843d75 = MapLightingVolume {
                sunColor: vec4 = { 0.486274511, 0.478431374, 0.498039216, 1 }
                sunDirection: vec3 = { 0.25, 0.827000022, 0.300000012 }
                0xd8851203: f32 = 75
                0xba02f116: f32 = 0.75
                skyLightColor: vec4 = { 0.56078434, 0.556862772, 0.458823532, 1 }
                horizonColor: vec4 = { 0.556862772, 0.58431375, 0.670588255, 1 }
                groundColor: vec4 = { 0.427450985, 0.501960814, 0.541176498, 1 }
                skyLightScale: f32 = 0.449999988
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.349019617, 0.309803933, 0.4627451, 1 }
                fogAlternateColor: vec4 = { 0.152941182, 0.192156866, 0.31764707, 1 }
                fogStartAndEnd: vec2 = { 600, -1750 }
                transform: mtx44 = {
                    3368.76636, 0, 0, 0
                    0, 5126.38379, 0, 0
                    0, 0, 3661.70264, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume1"
            }
            0x791a2f0f = MapGroup {
                transform: mtx44 = {
                    0.99406755, 0.10876447, 0, 0
                    -0.10876447, 0.99406755, 0, 0
                    0, 0, 1, 0
                    182.073914, -2018.32874, 4352.53418, 1
                }
                name: string = "group22"
            }
            0xb2c89ada = MapGroup {
                members: list2[string] = {
                    "390a685d-b8f4-4769-9767-fd5ac3ba1fe7"
                    "a1fc87f2-35ea-4892-8b62-b2f91ddf1b4d"
                    "be9c119b-1dc1-45c9-942b-cd41a64e0db4"
                    "b7d1cab3-bff8-4152-bfa0-1cf805b4acc0"
                    "2cc09863-8f6b-4301-b2bf-ae077c733172"
                    "4ca522e6-42ad-4ded-9751-cef319c038e2"
                    "3150ed4e-1032-46e9-ba6b-99d087d0f063"
                    "0d62057a-ec91-4035-896e-d73a3e630a49"
                    "7d3a4af0-add1-4db2-8230-39e2e3ef491d"
                    "566d909d-17fe-42ae-9f19-b587637a7fff"
                    "ab63e88f-0f47-4669-886e-39a607083f2a"
                    "da516e6a-3b2e-4165-a7f8-90fd7aa65e12"
                    "f96b8976-e016-4651-84c3-56cff2629164"
                    "1b1b52b9-e98e-44ca-a38e-af17a8eb2e4a"
                    "2f32bfff-6edd-4bf4-b431-db6e02ab0e28"
                    "fa1fdf64-ee58-46be-b93c-2e0ebe5a8d8b"
                    "6609e14f-36e0-480f-ae8d-33890894377d"
                    "2f88a4c3-2787-4420-a78d-a5c41651ec0d"
                    "0c84d5fa-4c0a-45bd-ab9b-81121ac2fb31"
                    "6bcd8dc4-3233-45e8-b29e-d5a3b7fc7a2b"
                    "93028ca9-4f20-4a60-bf95-dfd1f6d33dc8"
                    "186b6096-c347-4425-a647-6a3e68127b97"
                    "983ed939-4070-4b89-a116-b2820133bae1"
                    "cd92bb49-5c0c-446d-aa13-19c4576eb459"
                    "acc2ef1d-ea72-47c1-a38d-d1a88ceba817"
                    "67cc4b6b-cc5a-4afd-a131-1f81ac267908"
                    "c8c9f8d0-b580-4f47-9492-482ff6d2feb0"
                    "7adac8c1-b14c-4010-8edd-faf9a09ae96d"
                    "87a90c33-6e4a-4419-b155-8b0935550960"
                    "17357029-8746-404b-a3c5-a2a1e87f344a"
                    "0dfd618f-a130-4bff-bc90-df709763be40"
                    "fb12a3a9-8e35-47cd-a1ca-c99d195eb68a"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    260.68573, -2104.21094, -456.025879, 1
                }
                name: string = "group23"
            }
            0x29836091 = MapGroup {
                members: list2[string] = {
                    "93fedf10-ec6b-423f-afc9-382729264de5"
                    "e756d2f0-c37a-4e4a-8ecc-ec927769c1e1"
                    "3fcacb82-95bc-4fbe-912c-29b449bbdf40"
                    "3bae2864-3ef0-40a2-acbb-eac35255e012"
                    "59433cdc-eb0e-4496-ad4c-81a21a64218d"
                    "6f1791e0-92da-4498-a508-2bb68f319505"
                    "f27162f2-4498-45b6-a172-f680015784aa"
                }
                transform: mtx44 = {
                    1.18233931, 0, 0, 0
                    0, 1.18233931, 0, 0
                    0, 0, 1.18233931, 0
                    961.832703, -590.428345, 3965.81689, 1
                }
                name: string = "group24"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Jinx"
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
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x5a2b7425 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 1.4629122
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1001.99512, 587.765991, 1323.84912, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth1"
            }
            0x2c3a46a3 = MapPointLight {
                type: link = 0x55ee3022
                radiusScale: f32 = 1.4629122
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2985.14038, 478.881409, 2686.50073, 1
                }
                name: string = "Light_Brazier_Point_DragonEarth2"
            }
            0x3a88c45c = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.79999995
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -8.99191284, 133.981842, 2817.95557, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean3"
            }
            0xd27ec12c = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.85000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3349.31641, 236.95256, 2509.6394, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean4"
            }
            0x506aaa83 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.85000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3385.64551, 246.21489, 2796.28296, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean5"
            }
            0x8ba96cef = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.85000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3445.18945, 333.5289, 2636.8938, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean6"
            }
            0x79d0bcf8 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 1.23366451
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -95.487587, 613.051086, 1964.5343, 1
                }
                name: string = "Freljord_FG_Torch1"
            }
            0xe4531802 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.76025319
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    47.6902924, 142.983459, 1214.83191, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean7"
            }
            0x9291c0cd = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.479344189
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    407.811768, 192.009262, 2102.36426, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean8"
            }
            0x8d760b23 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.616607606
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3513.7915, -194.568665, 2233.91235, 1
                }
                name: string = "Freljord_FG_Torch4"
            }
            0x63bede56 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.616607606
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3513.7915, -194.568665, 3096.75952, 1
                }
                name: string = "Freljord_FG_Torch5"
            }
            0xade3527d = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.588873208
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1758.01611, -1150.36499, 2653.08545, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean9"
            }
            0x52e2f749 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.649043918
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1427.47046, -1077.81897, 2656.50903, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean10"
            }
            0xba8a317c = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.20625985
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    377.866241, 465.384644, 2643.42065, 1
                }
                name: string = "Freljord_FG_Highlight1"
            }
            0x17f21256 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.20625985
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3418.08813, -122.519165, 804.085266, 1
                }
                name: string = "Freljord_FG_Highlight2"
            }
            0xb9038ccf = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.20625985
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    377.866241, 465.384644, 1039.21338, 1
                }
                name: string = "Freljord_FG_Highlight3"
            }
            0x5216c4ba = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.46066666
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1680.24316, -102.870003, 363.493835, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean13"
            }
            0xb200d9a1 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.46066678
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2755.86792, -102.870003, 363.493835, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean14"
            }
            0x3d7cac49 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.46066678
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3600.34497, -102.870003, 1544.41602, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean15"
            }
            0xe52568e1 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.46066678
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2728.39697, -102.870003, 3786.25122, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean16"
            }
            0xb1f1b1da = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.46066678
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1659.52295, -102.870003, 3786.25122, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean17"
            }
            0x6967d11b = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.807466805
                intensityScale: f32 = 1.79999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    781.037415, 123.508163, 1834.29138, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean18"
            }
            0x9b01b92b = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.807466805
                intensityScale: f32 = 1.79999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    772.635254, 141.178162, 2443.88574, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean19"
            }
            0xe0bc7b8a = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.807466805
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    194.226318, 136.715408, 1655.52478, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean20"
            }
            0xec32ddae = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.335597128
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    892.993286, 180.64473, 1313.54553, 1
                }
                name: string = "Odyssey_LightBlue_Fill1"
            }
            0x299813c4 = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.335597128
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3048.6543, 180.64473, 2714.02197, 1
                }
                name: string = "Odyssey_LightBlue_Fill2"
            }
            0xd5dc5264 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.90356207
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3474.20239, 592.764893, 2022.49634, 1
                }
                name: string = "Freljord_FG_Highlight4"
            }
            0x60ec92fe = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 0.433549225
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    774.085327, 396.450592, 1861.3418, 1
                }
                name: string = "Odyssey_LightYellow_Fill1"
            }
            0xa6d4a77c = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 0.438872695
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3956.63354, 299.368774, 2592.73804, 1
                }
                name: string = "Odyssey_LightYellow_Fill2"
            }
            0x519d56b0 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.5188911
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1579.27551, -65.668808, 3933.29028, 1
                }
                name: string = "Freljord_FG_Highlight5"
            }
            0x634bc62d = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 2.4260366
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1616.22961, 356.793884, 23.302948, 1
                }
                name: string = "Freljord_FG_Highlight6"
            }
            0x72275271 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.811594069
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2198.73999, -102.870003, 658.088135, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean2"
            }
            0x5a40fdc0 = MapPointLight {
                type: link = 0xa963bb68
                radiusScale: f32 = 2.31383657
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2044.49121, 474.968201, 2025.12964, 1
                }
                name: string = "Odyssey_DesaturatedBlue_Center1"
            }
            0xe5a2e3bc = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 0.222531915
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3170.3728, 43.7905998, 1123.37585, 1
                }
                name: string = "Odyssey_LightYellow_Fill3"
            }
            0xe5f21a0a = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 0.222531915
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1177.66614, 43.7905998, 2718.84521, 1
                }
                name: string = "Odyssey_LightYellow_Fill4"
            }
            0x3102e83e = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.311048955
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    213.603394, 143.101639, 3074.57007, 1
                }
                name: string = "Odyssey_LightBlue_Fill3"
            }
            0xf6069f81 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.512831509
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    846.427673, 97.9466629, 3065.19043, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean1"
            }
            0x337aa98a = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.529606581
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    587.579834, -11.4831324, 3065.19043, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean21"
            }
            0x7879f0b6 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    846.427673, 97.9466629, 3065.19043, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean22"
            }
            0xfc6fbe22 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    587.579834, -11.4831324, 3065.19043, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean23"
            }
            0xf828643d = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.545821726
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    793.704773, -47.2133102, 2991.73144, 1
                }
                name: string = "Freljord_FG_Highlight7"
            }
            0x4252dec7 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.588873208
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1683.07507, -1492.1532, 2653.08545, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean25"
            }
            0x92c551b5 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.588873208
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1486.65759, -1483.66602, 1306.79993, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean11"
            }
            0x4e9720c8 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.588873208
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1738.41894, -1120.27795, 1306.79993, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean12"
            }
            0x63eee876 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.649043918
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1414.30652, -1181.54834, 1310.22351, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean24"
            }
            0x78227724 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.588873208
                intensityScale: f32 = 1.95000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1797.74365, -1418.68555, 1306.79993, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean26"
            }
            0xde0c9574 = MapPointLight {
                type: link = 0x62a42502
                radiusScale: f32 = 0.155967981
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3044.9563, 153.753815, 2440.04761, 1
                }
                name: string = "Odyssey_LightBlue_Fill4"
            }
            0x19ed0c13 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.263326675
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    611.802368, 94.9884186, 1151.16785, 1
                }
                name: string = "Freljord_FG_Highlight8"
            }
            0x4875a4c3 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.748539627
                intensityScale: f32 = 1.79999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2898.15918, -44.570488, 1477.28357, 1
                }
                name: string = "Freljord_FG_Highlight9"
            }
            0x637e73ba = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 1.5188911
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1813.67493, -529.996582, 4264.28857, 1
                }
                name: string = "Freljord_FG_Highlight10"
            }
            0x8c672173 = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 1.03320324
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1946.8103, 661.093628, 1113.91553, 1
                }
                name: string = "Odyssey_LightYellow_Fill5"
            }
            0x33210d5a = MapPointLight {
                type: link = 0x3e815b32
                radiusScale: f32 = 1.03320324
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1946.8103, 661.093628, 2900.14355, 1
                }
                name: string = "Odyssey_LightYellow_Fill6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Jinx"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x9029d950 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Jets"
                transform: mtx44 = {
                    0.561843872, 0.827243328, 0, 0
                    -0.827243328, 0.561843872, 0, 0
                    0, 0, 1, 0
                    3494.03296, 303.469086, 2634.85107, 1
                }
                name: string = "TFT_Odyssey_Jinx_Jets1"
            }
            0x668b7cf2 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Jets"
                transform: mtx44 = {
                    0.561843872, 0.827243328, 0, 0
                    -0.827243328, 0.561843872, 0, 0
                    0, 0, 1, 0
                    3395.39819, 215.11792, 2504.97705, 1
                }
                name: string = "TFT_Odyssey_Jinx_Jets2"
            }
            0xafef22cd = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Jets"
                transform: mtx44 = {
                    0.561843872, 0.827243328, 0, 0
                    -0.827243328, 0.561843872, 0, 0
                    0, 0, 1, 0
                    3438.3811, 213.346893, 2792.69092, 1
                }
                name: string = "TFT_Odyssey_Jinx_Jets3"
            }
            0x60d70cb7 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Hangar_Volume"
                transform: mtx44 = {
                    0.802807093, -0.596238911, 0, 0
                    0.596238911, 0.802807093, 0, 0
                    0, 0, 1.20000005, 0
                    314.326782, 870.463196, 1956.79797, 1
                }
                name: string = "TFT_Odyssey_Jinx_Hangar_Volume1"
            }
            0x604c2dec = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_ShipLightFog"
                transform: mtx44 = {
                    1.166641, 0, -0.942840815, 0
                    0, 1, 0, 0
                    0.628560543, 0, 0.777760684, 0
                    733.567993, 133.382019, 1869.74255, 1
                }
                name: string = "TFT_Odyssey_Jinx_ShipLightFog1"
            }
            0x1aa399e9 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_ShipLightFog"
                transform: mtx44 = {
                    0.777757585, 0, -0.628564298, 0
                    0, 1, 0, 0
                    0.628564298, 0, 0.777757585, 0
                    735.343689, 150.977753, 2478.34277, 1
                }
                name: string = "TFT_Odyssey_Jinx_ShipLightFog2"
            }
            0x2ee7961a = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_ShipLightFog"
                transform: mtx44 = {
                    0.777757585, 0, -0.628564298, 0
                    0, 1, 0, 0
                    0.628564298, 0, 0.777757585, 0
                    147.784729, 125.901581, 1675.11621, 1
                }
                name: string = "TFT_Odyssey_Jinx_ShipLightFog3"
            }
            0x4b018caf = null
            0x5e7fa2f8 = null
            0xbd4453e5 = null
            0xe4ede077 = null
            0x41f6a989 = null
            0x8485ac42 = null
            0xde201621 = null
            0x50e3631b = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString"
                transform: mtx44 = {
                    -0.337758422, 0.592634082, 0.73123467, 0
                    -0.472947061, 0.564833283, -0.676227927, 0
                    -0.813781381, -0.574236989, 0.089507319, 0
                    814.309998, 551.429993, 1027.09998, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString1"
            }
            0x9ad9b726 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString"
                transform: mtx44 = {
                    0.469855994, -0.87334758, 0.128449425, 0
                    0.787832558, 0.480512708, 0.385262579, 0
                    -0.398189753, -0.0798213109, 0.913823485, 0
                    711.909973, 456.619995, 1396.69995, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString2"
            }
            0xf04ac238 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale3"
                transform: mtx44 = {
                    -0.0819293708, 0.285345793, 0.954916358, 0
                    -0.118221626, 0.948590219, -0.293598533, 0
                    -0.989601493, -0.136946127, -0.0439833589, 0
                    654.040833, 639.989502, 1748.09875, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString3"
            }
            0xc3058450 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale2"
                transform: mtx44 = {
                    -0.0309281312, 0.235271692, -0.971437395, 0
                    0.00627297163, 0.971928835, 0.235191017, 0
                    0.999501824, 0.00118023157, -0.0315357968, 0
                    628.469971, 704.090759, 2356.70239, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString4"
            }
            0xc4ecfef3 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString"
                transform: mtx44 = {
                    -0.0309274346, 0.198564082, -0.979599774, 0
                    0.00627732277, 0.980087936, 0.198464841, 0
                    0.999501944, -1.12354755e-05, -0.0315580554, 0
                    628.469971, 757.150024, 2361.19995, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString5"
            }
            0xb5d1ccd6 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString_Scale2"
                transform: mtx44 = {
                    -0.165035933, 0.224422753, -0.960415304, 0
                    -0.0758801699, 0.967992783, 0.239232481, 0
                    0.983364344, 0.112358451, -0.142724335, 0
                    715.011658, 597.205627, 2885.12866, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString6"
            }
            0x97242b96 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_LightString"
                transform: mtx44 = {
                    0.055481758, -0.187784597, -0.980641961, 0
                    -0.417352259, 0.887875557, -0.193633169, 0
                    0.907049417, 0.420016259, -0.0291114282, 0
                    670, 781.150024, 2940.19995, 1
                }
                name: string = "TFT_Odyssey_Jinx_LightString7"
            }
            0x66904606 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Light_Flare"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1177.9292, 11.9056091, 2719.28735, 1
                }
                name: string = "TFT_Odyssey_Jinx_Light_Flare1"
            }
            0xbca3f2d3 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 0.96677357, 0.255634427, 0
                    0, -0.255634427, 0.96677357, 0
                    883.442444, 153.765396, 1460.43225, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens1"
            }
            0x23dfbf52 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -8.74227766e-08, 0, 0.99999994, 0
                    -0.207382411, 0.978259921, -1.81299473e-08, 0
                    -0.978259861, -0.207382426, -8.55221955e-08, 0
                    748.652039, 152.178299, 1335.31982, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens2"
            }
            0xa2672294 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -0.99999994, 2.22044605e-16, 8.74227766e-08, 0
                    -2.0013589e-08, 0.973443151, -0.22892876, 0
                    -8.51011066e-08, -0.228928775, -0.973443091, 0
                    3047.43555, 152.775558, 2544.97388, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens3"
            }
            0x8f1f7186 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    8.74227695e-08, 7.66053887e-15, -0.99999994, 0
                    0.224895552, 0.974382758, 1.96610035e-08, 0
                    0.974382699, -0.224895567, 8.51832453e-08, 0
                    3184.24316, 152.80603, 2666.53247, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens4"
            }
            0x8261c930 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Space_Mist"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2400.80005, -1710.96252, 89.1949463, 1
                }
                name: string = "TFT_Odyssey_Jinx_Space_Mist1"
            }
            0x8c1efe6e = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Sparks"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2964.77661, 2.11575317, 1380.85205, 1
                }
                name: string = "TFT_Odyssey_Jinx_Sparks1"
            }
            0xb4759853 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_ShootingStar"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1999.98035, 36.7548828, 1989.49426, 1
                }
                name: string = "TFT_Odyssey_Yasuo_ShootingStar1"
                0xccf79327: u8 = 126
            }
            0x5e913af3 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Yasuo/TFT_Odyssey_Yasuo_Ship"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2030.24683, -19.3151855, 2033.86475, 1
                }
                name: string = "TFT_Odyssey_Yasuo_Ship1"
                0xccf79327: u8 = 126
            }
            0x1a2f5e79 = null
            0x2df5dadd = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Light_Flare"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3171.18066, 17.0494766, 1124.35608, 1
                }
                name: string = "TFT_Odyssey_Jinx_Light_Flare3"
            }
            0x24f1428e = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1092.80457, 8.00003052, 1618.11279, 1
                }
                name: string = "TFT_GoldMine_Odyssey_Jinx_Start1"
            }
            0xc74cea79 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_GoldMine_Odyssey_Jinx_Start_Away"
                transform: mtx44 = {
                    -0.99999994, 0, 8.74227766e-08, 0
                    0, 1, 0, 0
                    -8.74227766e-08, 0, -0.99999994, 0
                    2899.65698, 8, 2427.54419, 1
                }
                name: string = "TFT_GoldMine_Odyssey_Jinx_Start_Away1"
            }
            0x0cb7c728 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster01"
                transform: mtx44 = {
                    0.977119505, 0.212691039, 0, 0
                    1.85940419e-08, -8.54224993e-08, 0.99999994, 0
                    0.212691024, -0.977119446, -8.74227766e-08, 0
                    1154.86475, -514.431824, 4079.09521, 1
                }
                name: string = "TFT_Odyssey_Jinx_Arena_JetThruster01_1"
            }
            0xbed00177 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Arena_JetThruster02"
                transform: mtx44 = {
                    0.977119505, 0.212691039, 0, 0
                    1.85940419e-08, -8.54224993e-08, 0.99999994, 0
                    0.212691024, -0.977119446, -8.74227766e-08, 0
                    1323.74011, -1010.5611, 4386.24707, 1
                }
                name: string = "TFT_Odyssey_Jinx_Arena_JetThruster02_1"
            }
            0x5684b1ad = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    -0.0190183297, -0.00454938551, 0.649705708, 0
                    -0.209489122, 0.772084057, -0.000725904538, 0
                    -0.964661777, -0.261769444, -0.0300707631, 0
                    742.202454, 143.953201, 1195.74304, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens5"
            }
            0xf729bfe5 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Odyssey_Jinx_Screens"
                transform: mtx44 = {
                    0.020521963, -0.00472160336, -0.64965874, 0
                    0.220773548, 0.768932581, 0.00138551579, 0
                    0.960648417, -0.27587676, 0.032350786, 0
                    3189.99902, 143.349396, 2816.76782, 1
                }
                name: string = "TFT_Odyssey_Jinx_Screens6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Jinx"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe6467383 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Common/TFT_Audio-Emitter_Odyssey_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1939.61841, -0.000366210938, 2464.07226, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Amb_Loop1"
            }
            0x20f6f240 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Jet_Thrusters"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3531.79736, 294.706421, 2573.56982, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Jinx_Jet_Thrusters1"
            }
            0x25cfdc4c = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Station_Amb"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    365.050171, 455.478027, 1325.18066, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Jinx_Station_Amb1"
            }
            0x0a5de603 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/Jinx/TFT_Audio-Emitter_Odyssey_Jinx_Amb2D"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2015.14734, -0.000122070312, 2054.9751, 1
                }
                name: string = "TFT_Audio-Emitter_Odyssey_Jinx_Amb2D1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Jinx"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x9c3ef054 = null
            0x83f38f50 = null
            0xfb87a23b = null
            0x6355e046 = null
            0x6dba7ec6 = null
            0xa47df37e = null
            0x5a703b44 = null
            0xdd1f35fb = null
            0xbd827774 = null
            0x7ecde1f3 = MapGroup {
                members: list2[string] = {
                    "594efba1-6230-4e81-ba78-722103e540e9"
                    "2c3e2d4e-f01a-42d7-8f72-33340777d4ad"
                    "ca8a2fec-4d22-4024-96c2-641f0b9fe632"
                    "aba938d6-7401-4b84-948a-e2f70b048f06"
                    "728b3664-09c7-40d9-bb26-4132a2241ec8"
                    "baa7b8e1-72bb-4b0f-b654-651b90d16059"
                    "1ba6d5d0-eca5-49e3-b658-95389ca1863b"
                    "ba57934f-63a9-4416-af9d-913f5fb6e140"
                }
                name: string = "group5"
            }
            0x5c9721b0 = null
            0x70a2c83a = null
            0x64891ee8 = null
            0x44573fe9 = null
            0xf71a9286 = null
            0xba698550 = null
            0x43663c5e = MapGroup {
                members: list2[string] = {
                    "2d7c7a1a-10a1-49f2-9549-31d68d46cc81"
                    "a003b632-b33b-49b9-937a-4f1877d5c0a7"
                }
                name: string = "group6"
            }
            0x79fefc20 = null
            0x890e6de8 = null
            0xdf422b2e = null
            0xa3f391d2 = null
            0x99cec71e = null
            0xe951e9ce = null
            0xc3bd80ba = null
            0xb3dacaf7 = null
            0xf3e236b0 = MapGroup {
                members: list2[string] = {
                    "9463414f-b00b-457e-8b20-c0a1627bc9ab"
                    "1fd77a9c-5593-496b-aae7-5fdb5e51ee34"
                    "715c7445-1ca5-4f8e-8e6c-42a4bc1ac8b6"
                    "ccb25d14-b2a5-4502-acb7-be553a689d93"
                    "9b56f1be-8fe6-4108-ae68-4f9c519aa009"
                    "442ef343-89a3-4804-a783-f0239653c2f2"
                    "94401db5-a1f0-460c-afbb-dc72454243ce"
                    "0a278e9b-7995-4e66-8500-8a7aa56226d3"
                    "10ce0ec9-9191-4f2d-91d8-15cb6112bf6a"
                    "903bc518-a0f4-46ef-a080-a11d93310dd2"
                    "b59485f9-e85d-433d-b20b-ed7c504ebaae"
                    "51322683-dbe8-466a-88d4-a16d178fded5"
                    "ecf2ff25-ec4f-4dcf-b882-d8c540bca02c"
                    "5c43c108-cc41-45e7-bfe5-20f49b9d45e5"
                    "581e6f85-a490-406e-8ee7-66e6dee8553a"
                    "0f62ab0f-34e4-4b74-bec2-1e90eb2adfde"
                    "2d4049b5-1b37-47f5-9e29-2d3604992ac9"
                    "fe64f51c-0ffb-4431-8207-085d3d2f6a8a"
                    "6ba24e4c-9122-4426-a8ad-80920b76f1fb"
                    "8033c680-6038-4d46-8648-491461a1ee3e"
                    "a997b543-60b9-48e4-a82b-c80dc494f45d"
                    "e9340e4c-4b08-4f80-b2b5-dacede3cc40f"
                    "ee99010f-2f2c-4665-8421-97ac4b1b1644"
                    "cb71e536-bc9b-4f12-8c66-118ee44c85a6"
                    "49edc4b5-2e23-4e14-b0e7-7105de0d3c78"
                    "ba873a9a-843d-4e1b-9e08-9b51417612c9"
                    "d8c187f6-71d5-41ac-bb31-72ed1bbc28c1"
                    "a6001ec9-36c1-4a69-8365-a140025499dd"
                    "cbc43c62-020d-4833-a364-1cdf29801e5d"
                    "916430b1-d8e7-40c6-83c2-6f4f3639e068"
                }
                name: string = "group7"
            }
            0xe20d8b96 = null
            0x70b1a0ff = null
            0x6e542861 = null
            0xf939a688 = null
            0x4f92fbf6 = null
            0x1e140ddd = null
            0xfa5dccc8 = null
            0x1d8ca989 = null
            0x515c64d6 = null
            0x931cb381 = null
            0x836d1127 = null
            0xda80d965 = null
            0x495826b0 = null
            0xe732d7db = null
            0x895c07e4 = null
            0x8f3d3524 = null
            0x589b806b = null
            0x044fc069 = null
            0x182453b9 = null
            0x728dfd48 = null
            0x56e84c47 = null
            0xcf1edeb6 = null
            0x26646977 = null
            0x479fd169 = null
            0x1fba13c5 = null
            0x21766b75 = null
            0xf7ab4603 = null
            0x7cb8b15f = null
            0x1007ffbe = null
            0x046b7967 = null
            0xc28aca3f = null
            0xded2230b = null
            0xa706bfcb = null
            0x3587ba76 = null
            0x021e427e = null
            0x11686611 = MapGroup {
                members: list2[string] = {
                    "fa82339d-e0c7-472c-9af5-e9018cd4e774"
                    "941f8eab-73ac-47e5-a116-a5407b1dc9b8"
                }
                name: string = "group8"
            }
            0xd9a12e61 = null
            0xed50d838 = null
            0x04b72208 = null
            0xeaaaf2d7 = null
            0x888d43a0 = null
            0x322f655a = null
            0xf55b9ed6 = null
            0x0bc8821e = null
            0xd9fcf4d1 = null
            0x0ab6bd88 = null
            0xd6a325a0 = null
            0x591cd823 = null
            0x1ef56612 = MapGroup {
                members: list2[string] = {
                    "bd77b56b-0385-4f14-b53b-f31eb5a39e4f"
                    "151f3bcb-94e3-42af-aa76-f0e12a32f77e"
                    "13ca7bf6-1d0f-4d67-ae73-42db8a88b10d"
                    "52f5659f-e665-418f-90fd-d8491fddade5"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1040.97327, 15.8358154, 2034.53284, 1
                }
                name: string = "group9"
            }
            0x8e11741e = null
            0xee105ff3 = null
            0x0548ebba = null
            0x2d527585 = null
            0x6e48fba3 = MapGroup {
                members: list2[string] = {
                    "04666afd-4964-4e0f-b54d-4ab03dee2719"
                    "0a8f121d-8c16-4ed5-ac67-3c6038c72e80"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1011.85791, 15.0855713, 2080.89819, 1
                }
                name: string = "group19"
            }
            0x22848e33 = null
            0xd07e997b = null
            0x7f934e5d = null
            0x5b74d82d = null
            0xdc6ea00b = null
            0x3cffe86c = null
            0x18c87544 = null
            0x9bfcdf10 = null
            0xf42dc056 = null
            0x75753a4d = null
            0x4c42a3e9 = null
            0xc969654e = null
            0xa6b57070 = null
            0x9fb25837 = null
            0xe3c621bb = null
            0xbe96ba6c = null
            0x966ad172 = MapGroup {
                members: list2[string] = {
                    "53b17cb9-a3d7-4834-921b-1ea30f5134e7"
                    "fa7540dd-d505-48f6-8866-a9438a553eac"
                    "521c707c-400e-4d2d-bc11-e5ef100d1fec"
                    "4bebaef5-92c8-4e91-8e7a-9583a04f1fbd"
                }
                transform: mtx44 = {
                    0.914000273, 0, -0.405715406, 0
                    0, 1, 0, 0
                    0.405715406, 0, 0.914000273, 0
                    3340.31812, -5.45227051, 3288.66675, 1
                }
                name: string = "group25"
            }
            0xf40a6119 = MapGroup {
                members: list2[string] = {
                    "a2f587c5-889c-43ed-af7b-de975918590c"
                }
                transform: mtx44 = {
                    -0.350199789, 0, -0.93667537, 0
                    0, 1, 0, 0
                    0.93667537, 0, -0.350199789, 0
                    2480.68188, -11.8686523, 1465.65747, 1
                }
                name: string = "group26"
            }
            0x496ee54d = null
            0xf8e95a0f = null
            0x0a107d59 = null
            0x41260d87 = MapGroup {
                transform: mtx44 = {
                    -0.999021709, 0, -0.0442254655, 0
                    0, 1, 0, 0
                    0.0442254655, 0, -0.999021709, 0
                    2308.2771, -2.60913086, 1343.43469, 1
                }
                name: string = "group27"
            }
            0xd10e88e6 = null
            0x5ce9a1e4 = null
            0x10308566 = MapGroup {
                members: list2[string] = {
                    "91c5fc0a-b23e-49cb-b9f4-f70968fb2b6c"
                    "5d08bb99-1c13-4710-8e9a-75351c3262a3"
                }
                transform: mtx44 = {
                    0.99977386, 0, -0.0212656762, 0
                    0, 1, 0, 0
                    0.0212656762, 0, 0.99977386, 0
                    2329.55688, -2.60908508, 1349.76331, 1
                }
                name: string = "group28"
            }
            0x0a588f55 = null
            0xc3d7a4c9 = null
            0xe31e3e04 = null
            0xa8db2220 = null
            0xf681d453 = MapGroup {
                members: list2[string] = {
                    "e01cc3ee-a911-4b7b-b64a-eb028f8c82fc"
                    "fbe4e186-ba86-4f8f-8c7d-bada66559ffb"
                    "134f5c87-bcfb-4828-8f3e-ac025148b328"
                    "0c211ca8-83a0-414d-a366-1a5503169c27"
                    "74bbd009-9f13-4a7a-964a-a5054b0b3a4f"
                    "815fbfd1-7f27-4092-906c-e51680216ca9"
                    "6d13dbc7-4917-4b47-a305-a7b6c2f329b6"
                    "bf278112-df0e-49bd-bbb9-70d96b11f42f"
                    "f1785800-0809-482c-a736-ef5283852dbb"
                    "bf062e5a-3799-444a-a7a8-73303e58ab90"
                    "e7b9c889-55de-443d-bb25-e4a3007fe3bd"
                }
                transform: mtx44 = {
                    1, 0, -4.76837158e-07, 0
                    0, 1, 0, 0
                    4.76837158e-07, 0, 1, 0
                    1902.09375, -400.789978, 3020.63965, 1
                }
                name: string = "group29"
            }
            0x350cffdf = null
            0x9df580aa = null
            0x00f0792b = null
            0x709439f1 = MapGroup {
                members: list2[string] = {
                    "4b6d03d0-af85-42e7-b1a4-3fc875210eb4"
                    "c82a0da9-bf4a-4450-94a8-0507006307be"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2109.7439, -5.23655701, 3723.11792, 1
                }
                name: string = "group30"
            }
            0x748d06f6 = MapGroup {
                members: list2[string] = {
                    "9aebdb6e-1943-451e-b7e0-062d93951df5"
                }
                transform: mtx44 = {
                    -0.122735128, 0, 0.992439985, 0
                    0, 1, 0, 0
                    -0.992439985, 0, -0.122735128, 0
                    931.536499, -15.0586853, 2510.03174, 1
                }
                name: string = "group31"
            }
            0x3a74e738 = null
            0x9084fdfc = null
            0xb87df394 = null
            0x744c9d0a = null
            0xae8dd3cb = MapGroup {
                transform: mtx44 = {
                    -0.370540977, 0, -0.928816438, 0
                    0, 1, 0, 0
                    0.928816438, 0, -0.370540977, 0
                    1185.34607, -0.00048828125, 2595.17871, 1
                }
                name: string = "group32"
            }
            0x8a854f5b = null
            0x5c1d65c5 = null
            0x1641db83 = null
            0x5bee5f89 = null
            0xba103279 = MapGroup {
                transform: mtx44 = {
                    1.35929, 0, 0, 0
                    0, 1.35929, 0, 0
                    0, 0, 1.35929, 0
                    3490.03247, 87.5688324, 2774.94482, 1
                }
                name: string = "group33"
            }
            0x31b79934 = MapGroup {
                transform: mtx44 = {
                    0.968897641, 0.24746187, 0, 0
                    -0.24746187, 0.968897641, 0, 0
                    0, 0, 1, 0
                    3490.03271, 122.007477, 2774.94385, 1
                }
                name: string = "group34"
            }
            0x5ea91442 = MapGroup {
                members: list2[string] = {
                    "b269c156-59f3-499f-8653-5140022ee3fd"
                    "59f6121a-aaef-4350-ab93-c91386a74126"
                    "0b3a2702-6acb-40b8-8063-6e725d4f8ae5"
                }
                transform: mtx44 = {
                    0.989057958, 0.0782729164, -0.125050604, 0
                    -0.0788921937, 0.996883154, 0, 0
                    0.124660842, 0.0098655168, 0.992150366, 0
                    3524.10083, 155.954926, 2487.07959, 1
                }
                name: string = "group35"
            }
            0xd6035927 = null
            0x4d15d950 = null
            0xcad7116c = null
            0xf9e0dcce = null
            0xebbdcc48 = null
            0xdea11f24 = null
            0x6289ffc9 = null
            0xa84bbf44 = null
            0x8a4a8e1d = null
            0x628e0500 = null
            0xb48718f7 = null
            0x1746bcbd = null
            0xd2e1a033 = null
            0x95b8f7bd = null
            0x6fb4b795 = null
            0xfd79192a = MapGroup {
                members: list2[string] = {
                    "91c5fc0a-b23e-49cb-b9f4-f70968fb2b6c"
                }
                transform: mtx44 = {
                    0.811420202, 0, 0, 0
                    0, 0.811420202, 0, 0
                    0, 0, 0.811420202, 0
                    1099.40918, -5.23631287, 1488.40698, 1
                }
                name: string = "group38"
            }
            0x47de12eb = null
            0xc820acbc = null
            0xfe903a82 = null
            0x165adaec = null
            0x9d8d5a43 = null
            0xe3823474 = null
            0x1e2da3c4 = MapGroup {
                members: list2[string] = {
                    "9229498d-ccba-453e-a204-5a2886e17673"
                }
                transform: mtx44 = {
                    0.999517083, 0, -0.031074116, 0
                    0, 1, 0, 0
                    0.031074116, 0, 0.999517083, 0
                    1196.32886, -1.51886809, 1469.72827, 1
                }
                name: string = "group39"
            }
            0x6d748b02 = MapGroup {
                members: list2[string] = {
                    "3d0cdf65-baa0-4915-b07a-ee4f2b21d5b6"
                }
                transform: mtx44 = {
                    0.882763922, 0, 0.0251582079, 0
                    0, 0.855565429, 0, 0
                    -0.0243731737, 0, 0.855218172, 0
                    2478.40527, -5.23644781, 1339.70813, 1
                }
                name: string = "group40"
            }
            0xae521194 = null
            0x2c9bcacd = null
            0x574f23d5 = null
            0xf7d8ce48 = null
            0xd521a46b = null
            0x6a2083e5 = null
            0x63a1e2e8 = null
            0xcdef3ac8 = null
            0x6c5d0a72 = null
            0xacdf7d9d = null
            0x6d714442 = null
            0x64fd15a6 = null
            0x7f649a63 = null
            0xede6eb2d = null
            0x3125d9d7 = null
            0xa551fcb1 = null
            0x372866b7 = null
            0x28e760fd = null
            0x283d9008 = null
            0x4d31b8b4 = null
            0x3a88ef98 = null
            0x4c226f27 = null
            0x59f53e94 = null
            0xeb4560f2 = null
            0xae474780 = null
            0x322bed8b = null
            0xee004572 = null
            0xbbabf7a8 = null
            0x597ad29e = null
            0x34f3645f = null
            0xe72c273c = null
            0x8279383b = null
            0x521924b5 = null
            0xdf59efd9 = null
            0x1fd0806e = null
            0x252de8f8 = null
            0xc6cb0efc = null
            0xfcfa9d8b = null
            0xa226dd4f = null
            0x06334665 = null
            0xf27d94a8 = null
            0x40c76a36 = null
            0x6df23fd7 = null
            0x662c7cce = null
            0x85b37e95 = null
            0x7783b424 = null
            0xc3d6b98c = null
            0x8780493a = null
            0x90daf282 = null
            0x064013d3 = null
            0x3d4ee328 = null
            0x1fc5887d = null
            0x3e3a8fb3 = null
            0xdac5d2e2 = null
            0x8945eedd = null
            0x2cb44a10 = null
            0x7e6016eb = null
            0x39b6dee1 = null
            0xa4a5ce93 = null
            0x070145a6 = null
            0x6f3ae89d = null
            0xb9a2827e = null
            0x56c2179a = null
            0x587e8ab4 = null
            0xf023a20e = null
            0x40f3bb8c = null
            0x9ce5f014 = null
            0xb0bc8ed4 = null
            0x018a686b = null
            0x2ec8903a = null
            0xd8bcbdc2 = null
            0x37a68059 = null
            0xca9e5903 = null
            0xf35569a4 = null
            0x356657fa = null
            0x21ef903a = null
            0x7a40e1dd = null
            0x36ab76c3 = null
            0xa049b21b = null
            0xaa654cfb = null
            0x95e99fd0 = null
            0x341cfd72 = null
            0x33a80199 = null
            0x7e3e86d0 = null
            0xded590ab = null
            0xafe46b3e = null
            0x68fa096b = null
            0x734414c3 = null
            0x341f708c = null
            0x94e9941f = null
            0x3519f786 = null
            0xbd051660 = null
            0x81f70e11 = null
            0x37f0644b = null
            0x2c57e256 = null
            0x5c66692c = null
            0x36d78c4d = null
            0x89e04264 = null
            0x554b5a84 = null
            0x95020482 = null
            0xb0aaeb54 = null
            0xaf09de5e = null
            0x7c1f6306 = null
            0x0335a18d = null
            0x5b145c8e = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Jinx"
    }
    "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Jinx" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe4295702 = MapParticle {
                system: link = "Maps/Particles/TFT/Odyssey/TFT_Skybox_Odyssey_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1979.63403, 38.7037354, 1991.74475, 1
                }
                name: string = "TFT_Skybox_Odyssey_A1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Jinx"
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
    "Maps/MapGeometry/Map22/Odyssey_Jinx" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Odyssey_Jinx"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.239215687, 0.211764708, 0.376470596, 1 }
                sunDirection: vec3 = { -0.377999991, 0.813000023, -0.444000006 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.482352942, 0.521568656, 0.741176486, 1 }
                horizonColor: vec4 = { 0.321568638, 0.286274523, 0.509803951, 1 }
                groundColor: vec4 = { 0.368627459, 0.219607845, 0.392156869, 1 }
                skyLightScale: f32 = 2
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.00784313772, 0.0156862754, 0.109803922, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
                surfaceAreaToShadowMapScale: f32 = 0.0299999993
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.20000005
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Odyssey_Jinx/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Odyssey_Jinx_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        chunks: map[hash,link] = {
            "Art_Shared" = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Shared"
            0x7fc0fbef = "Maps/MapGeometry/Map22/Chunks/Odyssey/LightingVolume_Jinx"
            "Lighting_A" = "Maps/MapGeometry/Map22/Chunks/Odyssey/Lighting_Jinx"
            0xcc1f3a7e = "Maps/MapGeometry/Map22/Chunks/Odyssey/Audio_Jinx"
            "Odyssey_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Odyssey/Odyssey_Design_Base"
            0xda5edcd4 = "Maps/MapGeometry/Map22/Chunks/Odyssey/VFX_Jinx"
            0x6ddc0bb3 = "Maps/MapGeometry/Map22/Chunks/Odyssey/Art_Jinx"
            0x30c493f6 = "Maps/MapGeometry/Map22/Chunks/Odyssey/Skybox_Jinx"
        }
    }
    0x3e815b32 = MapPointLightType {
        lightColor: vec4 = { 0.819607854, 0.819607854, 0.435294122, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x62a42502 = MapPointLightType {
        lightColor: vec4 = { 0.494117647, 0.917647064, 0.921568632, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xa963bb68 = MapPointLightType {
        lightColor: vec4 = { 0.31764707, 0.513725519, 0.525490224, 1 }
        Impact: i32 = 1
    }
    0x51710564 = MapPointLightType {
        lightColor: vec4 = { 0.890196085, 0.552941203, 0.949019611, 1 }
        radius: f32 = 519
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x52248cce = MapPointLightType {
        lightColor: vec4 = { 0.690196097, 0.227450982, 0.772549033, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x55ee3022 = MapPointLightType {
        lightColor: vec4 = { 0.70588237, 0.498039216, 0.0745098069, 1 }
        radius: f32 = 700
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xdc31003a = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.717647076, 0.823529422, 1 }
    }
}
