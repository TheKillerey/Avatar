#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Darkstar/Models/Board_Celestial_A/Materials/ENV_CelestialBase_Board_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Models/Board_Celestial_A/Materials/ENV_CelestialBase_Board_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Board_Celestial_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Particles/Textures/Darkstar_Skybox_Stars2.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Celestial_Board_Thickness.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture2"
                textureName: string = "ASSETS/Shared/Materials/Generic_Noise3.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureScale"
                value: vec4 = { 1000.00098, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureRate"
                value: vec4 = { 0, 0.00999999978, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Blend_BaseAndScrolling"
                value: vec4 = { 0.50999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0, 0.0862745121, 0.607843161, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Scale"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Rate"
                value: vec4 = { -0.0500000007, -0.100000001, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Boost"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Range"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_EFFECTS"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WORLDSCROLLING_FORDODGEMASK"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_DarkstarBase"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Models/POI_Celestial_Hand_A/Materials/ENV_CelestialBase_Head_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Models/POI_Celestial_Hand_A/Materials/ENV_CelestialBase_Head_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Head_Celestial_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Particles/Textures/Darkstar_Skybox_Stars2.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Celestial_Thickness.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture2"
                textureName: string = "ASSETS/Shared/Materials/TFT_Darkstar_Noise.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureScale"
                value: vec4 = { 1000.00098, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureRate"
                value: vec4 = { 0, 0.00999999978, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Blend_BaseAndScrolling"
                value: vec4 = { 0.69749999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0, 0.0862745121, 0.607843161, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Scale"
                value: vec4 = { 1750.00098, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Rate"
                value: vec4 = { -0.00999999978, -0.100000001, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Boost"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Range"
                value: vec4 = { 0.5, 3, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_EFFECTS"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WORLDSCROLLING_FORDODGEMASK"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_DarkstarBase"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Models/POI_Celestial_Hand_A/Materials/ENV_CelestialBase_Hand_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Models/POI_Celestial_Hand_A/Materials/ENV_CelestialBase_Hand_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Head_B.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Particles/Textures/Darkstar_Skybox_Stars2.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Thickness.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture2"
                textureName: string = "ASSETS/Shared/Materials/Generic_Noise3.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureScale"
                value: vec4 = { 975, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureRate"
                value: vec4 = { 0, 0.00999999978, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Blend_BaseAndScrolling"
                value: vec4 = { 0.795000017, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0, 0.0862745121, 0.607843161, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Scale"
                value: vec4 = { 250, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTexture2Rate"
                value: vec4 = { -0.100000001, 0.0199999996, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Boost"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Overlay_Range"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_EFFECTS"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_WORLDSCROLLING_FORDODGEMASK"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_DarkstarBase"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Models/POI_Hand_A/Materials/ENV_ScrollingColor_HandA_celestial_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Models/POI_Hand_A/Materials/ENV_ScrollingColor_HandA_celestial_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Scrolling_Texture"
                textureName: string = "ASSETS/Shared/Materials/Generic_Noise.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Color"
                value: vec4 = { 0.243137255, 0.470588237, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureScale"
                value: vec4 = { 857.501404, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingTextureRate"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingMask_Bias"
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollingMask_Sharpness"
                value: vec4 = { 0.449725002, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "FresnelSize"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_ScrollingColor"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_Floating_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_Floating_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Blackhole_Rock_A.TFT_ArenaSkin_DarkStar.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 85, 0, 0 }
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_B_Floating_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_B_Floating_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Flat_Top_B.TFT_ArenaSkin_DarkStar.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 85, 0, 0 }
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Flat_Top_B.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/POI_Head_Supernova_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/POI_Head_Supernova_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Head_Supernova_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_Floating_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_Floating_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Tall_A.TFT_ArenaSkin_DarkStar.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 85, 0, 0 }
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Perch_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Perch_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Perch_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Celestial_Rock_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Celestial_Rock_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Celestial_Rock_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Celestial_Rock_Floating_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Celestial_Rock_Floating_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Celestial_Rock_A.TFT_ArenaSkin_DarkStar.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 85, 0, 0 }
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Facade_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Facade_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Facade_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/POI_Head_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/POI_Head_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/POI_Head_B.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Rumble" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Rumble"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Rumble"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_rumble"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                                    1.5
                                    3.5
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
                emitterName: string = "North_Light_Mesh"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2.5, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 0 }
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
                                { 600, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Lights_03.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.500007629, 0.86999315, 0.949996173, 0.289997697 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.5
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.500007629, 0.86999315, 0.949996173, 0.289997697 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.796078444, 1, 1, 0 }
                            { 1, 0.970000744, 0.730006874, 0.530006886 }
                            { 0.352941185, 0.611764729, 1, 1 }
                            { 0.588235319, 0.384313732, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 1
                    deltaIn: f32 = 10
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {}
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3.5, 8 }
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
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3.5, 8 }
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
                            { 1, 1, 0.25 }
                            { 1, 1, 0.850000024 }
                            { 1, 0.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Lights.TFT_ArenaSkin_DarkStar.dds"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00100000005, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00100000005, 0 }
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
                texDiv: vec2 = { 10, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 4, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    -1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 4, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Light_UV_01.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0149999997, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0149999997, 0.0299999993 }
                        }
                    }
                }
                birthUVOffsetMult: embed = ValueVector2 {
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
                                    -0.25
                                    0.25
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
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
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
                                    1.5
                                    3.5
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
                emitterName: string = "North_Light_Mesh1"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2.5, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 0 }
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
                                { 600, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Lights_03.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.259998471, 0.60999465, 0.839993894, 0.880003035 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.5
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.259998471, 0.60999465, 0.839993894, 0.880003035 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.592156887, 1, 0.709803939, 0 }
                            { 1, 0.970000744, 0.730006874, 0.749996185 }
                            { 0.469993144, 0.790005326, 1, 0.86999315 }
                            { 0.607843161, 1, 0.850980401, 0 }
                        }
                    }
                }
                pass: i16 = -10
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 1
                    deltaIn: f32 = 10
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {}
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 8, 8 }
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
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 8, 8 }
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
                            { 1, 1, 0.25 }
                            { 1, 1, 0.850000024 }
                            { 1, 0.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Light_UV_01.TFT_ArenaSkin_DarkStar.dds"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00499999989, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00499999989, 0 }
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
                texDiv: vec2 = { 10, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.0250000004, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0250000004, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 4, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.5
                                    0.500999987
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    -1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 4, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Light_UV_01.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0199999996, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0199999996, 0.100000001 }
                        }
                    }
                }
                birthUVOffsetMult: embed = ValueVector2 {
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
                                    -0.25
                                    0.25
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
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
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
                                    0.600000024
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
                    1
                }
                emitterName: string = "brightMist"
                birthOrbitalVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
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
                            { 0, 4, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 12, 0 }
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
                            { 0, 12, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -300, 10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 800, 200, 60 }
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
                                { 800, 200, 60 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.800000012
                        }
                        values: list[f32] = {
                            0.400000006
                            0.0399999991
                            0
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
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
                            { 1, 1, 1, 0.500007629 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.449999988
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.733333349, 0.372549027, 0.886274517, 0 }
                            { 0.925490201, 0.490196079, 1, 0.580392182 }
                            { 0.37000075, 1, 0.900007606, 0.549996197 }
                            { 0.140001521, 0.889997721, 1, 0.639993906 }
                            { 0.109803922, 0.509803951, 1, 0 }
                        }
                    }
                }
                pass: i16 = -20
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
                    erosionFeatherOut: f32 = 0.200000003
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
                    constantValue: vec3 = { 450, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.899999976
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
                texture: string = "ASSETS/Shared/Particles/Morde_Base_Dust.TFT_Set4_Act2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
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
                                    0.300000012
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
                emitterName: string = "brightMotes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.100000001, 0 }
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
                                    0.400000006
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 4, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.75
                                }
                            }
                            VfxProbabilityTableData {}
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -100, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 800, 150, 100 }
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
                                { 800, 150, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.800000012
                        }
                        values: list[f32] = {
                            0.400000006
                            0.0399999991
                            0
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.505882382, 0.886274517, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0.258823544, 0 }
                            { 0.4627451, 1, 0.101960786, 1 }
                            { 0.34117648, 0.749019623, 1, 0.960784316 }
                            { 0.101960786, 0.34117648, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
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
                                    0.800000012
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
                            { 0.0700000003, 0.985724688, 0.985724688 }
                            { 0.5, 0.972591341, 0.972591341 }
                            { 0.0863309354, 0.958887041, 0.958887041 }
                            { 0.800000012, 0.945182741, 0.945182741 }
                            { 0.300000012, 0.905592442, 0.905592442 }
                            { 0.699999988, 0.870570302, 0.870570302 }
                            { 0.25179857, 0.834025502, 0.834025502 }
                            { 0.99000001, 0.803571463, 0.803571463 }
                            { 0.140000001, 0.739617944, 0.739617944 }
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
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                                    1.5
                                    3.5
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
                emitterName: string = "North_Light_Mesh3"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 2.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2.5, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 0 }
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
                                { 600, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Lights_02.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.190005347, 0.659998477, 0.949996173, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.5
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.659998477, 0.949996173, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.796078444, 1, 1, 0 }
                            { 1, 0.970000744, 0.730006874, 0.530006886 }
                            { 0.352941185, 0.611764729, 1, 1 }
                            { 0.588235319, 0.384313732, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 1
                    deltaIn: f32 = 10
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.192156866, 1, 1, 1 }
                    fresnel: f32 = 0.200000003
                    fresnelColor: vec4 = { 0.0196078438, 1, 0.458823532, 0 }
                }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 8, 8 }
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
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 8, 8 }
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
                            { 1, 1, 0.25 }
                            { 1, 1, 0.850000024 }
                            { 1, 0.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_UV_04.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00100000005, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                }
                                keyValues: list[f32] = {
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00100000005, 0 }
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
                texDiv: vec2 = { 3, -1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0.00999999978 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, 0.00999999978 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500999987
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    -1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 3, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/common_color-celestial.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0149999997, 0.0299999993 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0149999997, 0.0299999993 }
                        }
                    }
                }
                birthUVOffsetMult: embed = ValueVector2 {
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
                                    -0.25
                                    0.25
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
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
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
                                    0.300000012
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
                emitterName: string = "brightMotes1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 15 }
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
                                    0.200000003
                                    1.25
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
                            { 10, 1, 15 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 800, 150, 100 }
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
                                { 800, 150, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.800000012
                        }
                        values: list[f32] = {
                            0.400000006
                            0.0399999991
                            0
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0.258823544, 0 }
                            { 0.223529413, 1, 0.137254909, 1 }
                            { 0.180392161, 1, 0.729411781, 0.960784316 }
                            { 0.101960786, 0.34117648, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 10, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.699999988
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 10, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0465116277
                            0.0491551459
                            0.0737327188
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
                            { 0.0719424486, 0.999026358, 0.999026358 }
                            { 0.827338159, 0.98997438, 0.98997438 }
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
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStarMode_Varus_Skin06_Specs_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                                    0.600000024
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
                    1
                }
                emitterName: string = "brightMist1_add"
                birthOrbitalVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
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
                            { 0, 4, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 12, 0 }
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
                            { 0, 12, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -280, 10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 800, 200, 60 }
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
                                { 800, 200, 60 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.800000012
                        }
                        values: list[f32] = {
                            0.400000006
                            0.0399999991
                            0
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.710002303, 0.289997697, 1, 0.829999208 }
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
                            { 0.710002303, 0.289997697, 1, 0.829999208 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.449999988
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.956862748, 0.458823532, 1, 0 }
                            { 0.650003791, 0.409994662, 1, 0.76000613 }
                            { 0.37000075, 1, 0.900007606, 0.360006094 }
                            { 0.130006865, 0.409994662, 1, 0.310002297 }
                            { 0.219607845, 0.321568638, 1, 0 }
                        }
                    }
                }
                pass: i16 = -20
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
                    erosionFeatherOut: f32 = 0.200000003
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
                    constantValue: vec3 = { 330, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 330, 1, 0 }
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2.5, 0 }
                }
                lingerVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.25, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -200, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 80, 0 }
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
                                { 600, 80, 0 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Celestial_Northern_Lights_03.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.310002297, 0.839993894, 0.76000613, 0.37000075 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.5
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.310002297, 0.839993894, 0.76000613, 0.37000075 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.779999971
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
                pass: i16 = -5
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 12, 8 }
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
                                    0.25
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 12, 8 }
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
                            { 1, 1, 0.25 }
                            { 1, 1, 0.850000024 }
                            { 1, 0.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_UV_06.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.720000029, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    -0.150000006
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.720000029, 0 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/common_color-celestial.TFT_ArenaSkin_DarkStar.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
            }
        }
        visibilityRadius: f32 = 500
        particleName: string = "Northern_Lights_Celestial"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_cosmic_twinkles"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Wind" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Wind"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Wind"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_cosmic_wind"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Skybox_Darkstar_B" = VfxSystemDefinitionData {
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
                pass: i16 = -12
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_Stars.dds"
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
                    constantValue: vec4 = { 0.360006094, 0.940001547, 1, 0.37000075 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.519996941, 1, 0.489997715, 0.590005338 }
                }
                pass: i16 = -6
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.400000006, 0 }
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
                    constantValue: vec2 = { 3, 6 }
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
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 290, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.305882365, 1, 0.619607866, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.889997721, 1 }
                }
                pass: i16 = -5
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
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 280, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.262745112, 1, 0.533333361, 0.972549021 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.352941185, 0.913725495, 1, 1 }
                }
                pass: i16 = -4
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
                    constantValue: vec4 = { 0.409994662, 0.970000744, 0.889997721, 0.60999465 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 1, 0.940001547, 0.600000024 }
                }
                pass: i16 = -9
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.239999995, 0.239999995, 0.239999995 }
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
                emitterName: string = "Star_Detail1"
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.710002303 }
                }
                pass: i16 = -11
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.100000001, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_StarsC.dds"
                texDiv: vec2 = { 2, 2 }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -1
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
                emitterName: string = "Star_Detail2"
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.469993144 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.330006868 }
                }
                pass: i16 = -10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.300000012, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
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
                emitterName: string = "Glow1"
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
                    constantValue: vec4 = { 0.409994662, 0.970000744, 0.889997721, 0.880003035 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 1, 0.940001547, 0.960006118 }
                }
                pass: i16 = -8
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.180000007, 0.180000007, 0.180000007 }
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
        particleName: string = "TFT_Skybox_Darkstar_B"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Skybox_Darkstar_B"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Glassy_Wisps" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Glassy_Wisps"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Glassy_Wisps"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_common_glassy_wisps"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Tones" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Tones"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Tones"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_cosmic_tones"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_DarkStar_Celestial_Burning_Neck" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                                    0.600000024
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
                    1
                }
                emitterName: string = "brightMist"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.400000006, 0 }
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
                            { 0, 0.400000006, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 0 }
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
                            { 1, 2, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -8, 8, 0 }
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
                            { -8, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 5, 0 }
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
                                { 180, 5, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
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
                            { 1, 1, 1, 0.300007641 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.643137276, 1, 0.75686276, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.219423294, 0.945098042, 0.75686276, 0 }
                            { 0.166459054, 0.964705884, 0.75686276, 1 }
                            { 0, 0.450980395, 0.75686276, 1 }
                            { 0, 0.298039228, 0.75686276, 0 }
                        }
                    }
                }
                pass: i16 = -5
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
                    erosionFeatherOut: f32 = 0.200000003
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
                    constantValue: vec3 = { 250, 1, 0 }
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
                            { 250, 1, 0 }
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
                    constantValue: f32 = 8
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
                    1
                }
                emitterName: string = "brightMistEdge"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            { 1, 1, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -8, 6, 0 }
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
                            { -8, 6, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 250, 5, 0 }
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
                                { 250, 5, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
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
                            { 1, 1, 1, 0.200000003 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.643137276, 1, 0.75686276, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.219423294, 0.945098042, 0.75686276, 0 }
                            { 0.166459054, 0.964705884, 0.75686276, 1 }
                            { 0, 0.450980395, 0.75686276, 1 }
                            { 0, 0.298039228, 0.75686276, 0 }
                        }
                    }
                }
                pass: i16 = -5
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
                    erosionFeatherOut: f32 = 0.200000003
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
                    constantValue: vec3 = { 100, 1, 0 }
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
                            { 100, 1, 0 }
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
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 15
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
                            15
                        }
                    }
                }
                emitterName: string = "brightMotes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -10, 10, 0 }
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
                            { -10, 10, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, -50 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 200, 0, 0 }
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
                                { 200, 0, 0 }
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { -10, 0, 45 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 1, 0.396078438, 0 }
                            { 0.784313738, 1, 0.192156866, 1 }
                            { 0, 0.917647064, 1, 0.450980395 }
                            { 0.00392156886, 0.152941182, 1, 0 }
                        }
                    }
                }
                pass: i16 = -6
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 1 }
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
                            { 50, 10, 1 }
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
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 15
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
                            15
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "darkMist"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 0 }
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
                            { 1, 2, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -4, 4, 0 }
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
                            { -4, 4, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 5, 0 }
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
                                { 180, 5, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
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
                            { 1, 1, 1, 0.300007641 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.333333343, 0.788235307, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0.788235307, 1, 0 }
                            { 0.333333343, 0.788235307, 1, 1 }
                            { 0.149019614, 0.358569771, 1, 1 }
                            { 0.0496732034, 0.160738185, 1, 0 }
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
                    constantValue: vec3 = { 250, 1, 0 }
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
                            { 250, 1, 0 }
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
                    constantValue: f32 = 4
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
                    1
                }
                emitterName: string = "darkMistEdge"
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
                    constantValue: vec3 = { 1, 2, 0 }
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
                            { 1, 2, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -4, 6, 0 }
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
                            { -4, 6, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 250, 5, 0 }
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
                                { 250, 5, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
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
                            { 1, 1, 1, 0.200000003 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.333333343, 0.788235307, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0.788235307, 1, 0 }
                            { 0.333333343, 0.788235307, 1, 1 }
                            { 0.0980392173, 0.361660898, 1, 1 }
                            { 0.0496732034, 0.160738185, 1, 0 }
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
                    constantValue: vec3 = { 100, 1, 0 }
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
                            { 100, 1, 0 }
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
        }
        particleName: string = "TFT_DarkStar_Celestial_Burning_Neck"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_DarkStar_Celestial_Burning_Neck"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/Large_Burning_Hair_Celestial" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                                    0.600000024
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
                    1
                }
                emitterName: string = "brightMist"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.800000012, 0 }
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
                            { 0, 0.800000012, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 0 }
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
                            { 1, 5, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -15, 15, 0 }
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
                            { -15, 15, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 5, 0 }
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
                                { 150, 5, 0 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
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
                    constantValue: vec4 = { 0.643137276, 1, 0.75686276, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.219423294, 0.945098042, 0.75686276, 0 }
                            { 0.166459054, 0.964705884, 0.75686276, 1 }
                            { 0, 0.450980395, 0.75686276, 1 }
                            { 0, 0.298039228, 0.75686276, 0 }
                        }
                    }
                }
                pass: i16 = -5
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
                    erosionFeatherOut: f32 = 0.200000003
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
                    constantValue: vec3 = { 250, 1, 0 }
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
                            { 250, 1, 0 }
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
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Base_Swirls_Fire"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 25 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Crown_Energy_Cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 1, 0.549019635, 0 }
                            { 0, 0.517647088, 1, 1 }
                            { 0, 0.31764707, 1, 0 }
                        }
                    }
                }
                useLingerColor: flag = true
                lingerColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec4] = {
                            { 1, 0.450980395, 0, 1 }
                            { 0.137254909, 0.121568628, 0.215686277, 0 }
                        }
                    }
                }
                pass: i16 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 30
                    deltaIn: f32 = 30
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
                                2
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0
                    erosionFeatherOut: f32 = 0.5
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Galio/Skins/Skin13/Particles/Galio_Q_Tar_Tornado_BurstWind_Erosion_V01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 0, 45 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.4000001, 5, 2.4000001 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT2_Hex_Inferno_FireRing.TFT_EnchantedHexes.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -0.5 }
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
                            { 1, -0.5 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.0250000004, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0250000004, 0.100000001 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/common_color-celestial.TFT_ArenaSkin_DarkStar.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
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
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 50000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 10
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 5
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "impactStones_smoke"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -20, 20, 0 }
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
                            { -20, 20, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, -50 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 0, 0 }
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
                                { 180, 0, 0 }
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { -10, 0, 45 }
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
                                    0.200000003
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
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0392156877, 1, 0.470588237, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.0392156877, 1, 0.470588237, 0 }
                            { 0.0392156877, 1, 0.470588237, 0.200000003 }
                            { 0.0250978004, 0.349996179, 0.470588237, 1 }
                            { 0.0366013087, 0, 0.470588237, 0 }
                        }
                    }
                }
                pass: i16 = -6
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 15, 10 }
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
                        values: list[vec3] = {
                            { 10, 15, 10 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_PDM_Cosmic_Spark_2x2.TFT_Set3.dds"
                numFrames: u16 = 3
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 16
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
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
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
                            { 0, 2, 0 }
                        }
                    }
                }
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
                        constantValue: vec3 = { 260, 5, 0 }
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
                                { 260, 5, 0 }
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.800000012, 0, 1, 0 }
                            { 0.533333361, 0, 1, 0.600000024 }
                            { 0.282352954, 0, 1, 0.479999989 }
                            { 0, 0.0470588244, 1, 0 }
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
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 1, 1 }
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
                            { 200, 1, 1 }
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
                            { 0.150000006, 0.300000012, 0.300000012 }
                            { 0.300000012, 0.600000024, 0.600000024 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Base_Env_MB_brazierFire_flipbook_01.TFT_ArenaSkin_Darkstar.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Env_MB_brazierFire_mult_Inaction.TFT_ArenaSkin_Darkstar.dds"
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "fireSwirlIn"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.101960786, 0.956862748, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.101960786, 0.956862748, 0 }
                            { 0.90196079, 0.0831680149, 0.956862748, 0.800000012 }
                            { 0.592156887, 0.0239907727, 0.956862748, 0 }
                        }
                    }
                }
                pass: i16 = -9
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
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
                            { 90, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 420, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT2_Hex_Inferno_RingGlow.TFT_EnchantedHexes.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.60000002
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Base_Swirls_Fire1"
                disabled: bool = true
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Garen/Skins/Skin13/Particles/Garen_Skin13_expo_cylinder.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.0549019612, 0.921568632, 0 }
                            { 0.835294127, 0, 1, 1 }
                            { 0.58431375, 0, 1, 0 }
                        }
                    }
                }
                useLingerColor: flag = true
                lingerColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                        }
                        values: list[vec4] = {
                            { 1, 0.450980395, 0, 1 }
                            { 0.137254909, 0.121568628, 0.215686277, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0
                    erosionFeatherOut: f32 = 0.5
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Galio/Skins/Skin13/Particles/Galio_Q_Tar_Tornado_BurstWind_Erosion_V01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isRotationEnabled: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
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
                            { 0, -50, 0 }
                        }
                    }
                }
                0x6861179c: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.899999976
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                            { 0, 2, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 2, 1.60000002 }
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
                        values: list[vec3] = {
                            { 1.60000002, 2, 1.60000002 }
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
                            { 1.5, 1, 1.5 }
                            { 1.70000005, 3, 1.70000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT2_Hex_Inferno_FireRing.TFT_EnchantedHexes.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec2] = {
                            { 0, 1.20000005 }
                            { 0, 0.400000006 }
                            { 0, 0 }
                            { 0, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/common_color-stardust.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
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
                emitterName: string = "darkMotes"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -20, 20, 0 }
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
                            { -20, 20, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, -50 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 0, 0 }
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
                                { 180, 0, 0 }
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { -10, 0, 45 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.298039228, 0.298039228, 0.298039228, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.298039228, 0, 0.14843522, 0 }
                            { 0.298039228, 0, 0.14843522, 1 }
                            { 0.298039228, 0, 0.128565937, 0.450980395 }
                            { 0.134409845, 0, 0.298039228, 0 }
                        }
                    }
                }
                pass: i16 = -6
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 1 }
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
                            { 10, 10, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.506976724
                            0.610852718
                            0.638759673
                            0.700775206
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.258992791, 0.616279066, 0.616279066 }
                            { 0.877697825, 0.486434102, 0.486434102 }
                            { 0.223021582, 0.451550394, 0.451550394 }
                            { 0.381294966, 0.374031007, 0.374031007 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Dmg_Skin03_Glow.TFT_Set3.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 15
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
                            15
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "darkMist"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
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
                            { 0, 0.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 0 }
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
                            { 1, 5, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -8, 8, 0 }
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
                            { -8, 8, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 5, 0 }
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
                                { 150, 5, 0 }
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
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
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
                            { 1, 1, 1, 0.800000012 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.333333343, 0.788235307, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.318181813
                            0.894545436
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0.788235307, 1, 0 }
                            { 0.333333343, 0.788235307, 1, 1 }
                            { 0.149019614, 0.358569771, 1, 1 }
                            { 0.0496732034, 0.160738185, 1, 0 }
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
                    constantValue: vec3 = { 250, 1, 0 }
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
                            { 250, 1, 0 }
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
                    constantValue: f32 = 5
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
                                    0.300000012
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
                emitterName: string = "brightMotes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -10, 10, 0 }
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
                            { -10, 10, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, -50 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 0, 0 }
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
                                { 180, 0, 0 }
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { -10, 0, 45 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 1, 0.396078438, 0 }
                            { 0.784313738, 1, 0.192156866, 1 }
                            { 0, 0.917647064, 1, 0.450980395 }
                            { 0.00392156886, 0.152941182, 1, 0 }
                        }
                    }
                }
                pass: i16 = -6
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 10, 1 }
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
                            { 70, 10, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0465116277
                            0.0491551459
                            0.0737327188
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
                            { 0.0719424486, 0.999026358, 0.999026358 }
                            { 0.827338159, 0.98997438, 0.98997438 }
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
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                                    0.300000012
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
                emitterName: string = "brightMotes1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
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
                            { 0, 0.200000003, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
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
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -10, 10, 0 }
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
                            { -10, 10, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 50, -50 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 180, 0, 0 }
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
                                { 180, 0, 0 }
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { -10, 0, 45 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 1, 0.396078438, 0 }
                            { 0.784313738, 1, 0.192156866, 1 }
                            { 0, 0.917647064, 1, 0.450980395 }
                            { 0.00392156886, 0.152941182, 1, 0 }
                        }
                    }
                }
                pass: i16 = -6
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 10, 1 }
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
                            { 60, 10, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0465116277
                            0.0491551459
                            0.0737327188
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
                            { 0.0719424486, 0.999026358, 0.999026358 }
                            { 0.827338159, 0.98997438, 0.98997438 }
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
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStarMode_Varus_Skin06_Specs_02.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Large_Burning_Hair_Celestial"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/Large_Burning_Hair_Celestial"
        soundOnCreateDefault: string = "Play_sfx_tft_env_darkstar_common_fire"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_common_fire"
        flags: u8 = 212
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Amb_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Amb_Loop"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Amb_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_amb_loop"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/DarkStar_Eyes_Celestial" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 15
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
                            15
                        }
                    }
                }
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Janna/Skins/Skin13/Particles/common_fireball.scb"
                        mLockMeshToAttachment: bool = true
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
                                    0.300000012
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
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.388235301, 0.921568632, 1, 0 }
                            { 0.349019617, 0.741176486, 1, 0.400000006 }
                            { 0.447058827, 0.447058827, 1, 0.400000006 }
                            { 0.670588255, 0.447058827, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 5
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.5
                    erosionMapName: string = "ASSETS/Perks/Styles/Inspiration/GlacialAugment/Particles/Perks_GlacialAugment_Slow_Avatar.dds"
                }
                depthBiasFactors: vec2 = { -1, -1 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 6, 6 }
                }
                texture: string = "ASSETS/Perks/Styles/Inspiration/GlacialAugment/Particles/Perks_GlacialAugment_Slow_Avatar.dds"
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
                texDiv: vec2 = { 0.75, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
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
                emitterName: string = "Sheild_Idle"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/Base_Sphere_Mesh.TFT_ArenaSkin_DarkStar.scb"
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
                    constantValue: vec4 = { 0.280003041, 0.770000756, 1, 0.700007617 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.280003041, 0.770000756, 1, 0 }
                            { 0.280003041, 0.770000756, 1, 0.700007617 }
                            { 0.278905004, 0.766981125, 0.996078432, 0.700007617 }
                            { 0.280003041, 0.770000756, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 5
                }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.610000014, 0.709999979, 0.709999979 }
                }
                scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Base_Sphere.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
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
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Base_Nebula_Mult.TFT_ArenaSkin_DarkStar.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0.0199999996 }
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
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.00999999978, 0.0199999996 }
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
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                                    0.300000012
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
                emitterName: string = "brightMotes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0.200000003 }
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
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0.200000003 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                shape: embed = VfxShape {
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
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 1, 0, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.707976997
                            1
                        }
                        values: list[vec4] = {
                            { 0.423529416, 1, 0.443137258, 0 }
                            { 0.384313732, 1, 0.403921574, 0.800000012 }
                            { 0.203921571, 0.615686297, 1, 0.360784322 }
                            { 0.356862754, 0.309803933, 1, 0 }
                        }
                    }
                }
                pass: i16 = -6
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 1 }
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
                            { 50, 10, 1 }
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
                                    0.25
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
                particleLifetime: embed = ValueFloat {
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
                            3
                        }
                    }
                }
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.494117647, 0.917647064, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.45730105, 0.313079596, 1, 0 }
                            { 0.494117647, 0.917647064, 1, 1 }
                            { 0.45730105, 0.313079596, 1, 0 }
                        }
                    }
                }
                pass: i16 = 106
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 360, 0 }
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
                            { 90, 360, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 500, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 200, 500, 1 }
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
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0, 2, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Leona/Skins/Skin12/Particles/Leona_Skin12_Halo_2.PIE_C_10_1.dds"
            }
        }
        particleName: string = "DarkStar_Eyes_Celestial"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/DarkStar_Eyes_Celestial"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Flute" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Flute"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Flute"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_cosmic_flute"
    }
    "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Arps" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Arps"
        particlePath: string = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Arps"
        soundPersistentDefault: string = "Play_sfx_tft_env_darkstar_celestial_cosmic_arps"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/Darkstar_Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2973.37793, 3, 2456.99707, 1
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
                    1037.88403, 0, 1629.42505, 1
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
                    2791.72803, 0, 2932.98193, 1
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
                    1203, 0, 1161.23303, 1
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
                    3040.00464, 0, 2849.18701, 1
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
                    867.638123, 0, 1226.63965, 1
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
                    1393.57202, 0, 1467.33997, 1
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
                    -0.99999994, 8.74227766e-08, 0, 0
                    8.74227695e-08, 0.999999881, 8.74227766e-08, 0
                    7.64274186e-15, 8.74227695e-08, -0.99999994, 0
                    2067, 0, 2427.01294, 1
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
                    1142.53601, 0, 1347.20203, 1
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
                    2863.53394, 0, 2696.646, 1
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
                    2000, 0, 1935.94604, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/Darkstar_Design_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/Lighting_Celestial" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x34fabace = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.843113363
                intensityScale: f32 = 1.95000005
                overrideCastStaticShadows: option[bool] = {
                    false
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    858.964722, -67.7343445, 940.216797, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean10"
            }
            0x271a1f96 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.25
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    382.649109, 756.394409, 2763.78613, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean15"
            }
            0x5dae96fd = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.11728168
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1238.44104, 570.059265, 2575.72558, 1
                }
                name: string = "Light_Point_Center_DragonCloud1"
            }
            0x225ddbbd = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.25295496
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3209.03955, -135.089111, 2897.52417, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean1"
            }
            0xeb8d53c3 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.988549531
                intensityScale: f32 = 1.02499998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2891.93677, 341.56665, 2650.66992, 1
                }
                name: string = "Light_Point_Center_DragonCloud2"
            }
            0xf3f037cd = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.943258047
                intensityScale: f32 = 1.125
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1109.96973, 342.294312, 1388.85986, 1
                }
                name: string = "Light_Point_Center_DragonCloud3"
            }
            0xf07df307 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.59999967
                intensityScale: f32 = 1.35000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2062.45117, 552.416016, 2064.67041, 1
                }
                name: string = "Light_Point_Center_DragonCloud4"
            }
            0x61bea5f8 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.826393902
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3107.84009, -238.898193, 1342.00415, 1
                }
                name: string = "Freljord_WC_Blue_Fill1"
            }
            0xa2f3cec4 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.23708868
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1899.47449, 436.022003, 1092.43298, 1
                }
                name: string = "Light_Point_Center_DragonCloud5"
            }
            0xc4daa364 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 1.30140817
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.79297, 436.022003, 2999.80005, 1
                }
                name: string = "Light_Point_Center_DragonCloud6"
            }
            0x7df04b9b = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1328.34448, -282.355927, 564.065918, 1
                }
                name: string = "Freljord_WC_Blue_Fill5"
            }
            0x4201f209 = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2506.76831, 789.67041, 87.1638336, 1
                }
                name: string = "Light_Point_Center_DragonCloud7"
            }
            0x7ecb8833 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.826393902
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    519.122681, -238.898193, 1342.00415, 1
                }
                name: string = "Freljord_WC_Blue_Fill2"
            }
            0xdba1fc37 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.826393902
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2341.00415, -238.898193, 807.981506, 1
                }
                name: string = "Freljord_WC_Blue_Fill3"
            }
            0x940deb86 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.826393902
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3318.82349, -292.39212, 2857.04858, 1
                }
                name: string = "Freljord_WC_Blue_Fill6"
            }
            0x1c498422 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.826393902
                intensityScale: f32 = 1.89999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2140.6355, -323.171082, 3462.77686, 1
                }
                name: string = "Freljord_WC_Blue_Fill4"
            }
            0xf390e159 = MapPointLight {
                type: link = 0x925f06fe
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1285.04468, 721.955078, 3309.47119, 1
                }
                name: string = "Freljord_WC_Center1"
            }
            0x4d7ce608 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 1.14809024
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3001.22534, 98.4982452, 1396.35266, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean3"
            }
            0x83200afd = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.528205454
                intensityScale: f32 = 1.10000002
                overrideCastStaticShadows: option[bool] = {
                    false
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    821.67926, 419.047882, 2518.31152, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean4"
            }
            0x676ed763 = MapPointLight {
                type: link = 0xdc31003a
                radiusScale: f32 = 0.528205454
                intensityScale: f32 = 0.850000024
                overrideCastStaticShadows: option[bool] = {
                    false
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    620.388367, 222.177322, 2407.06836, 1
                }
                name: string = "Light_Point_Brazier_DragonOcean5"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/Lighting_Celestial"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xee7ea060 = null
            0xebbbb7ae = null
            0x3cf1754b = null
            0xf41b7da2 = null
            0x0e68331a = null
            0xb3387e98 = null
            0x8888c35c = null
            0x5998b2d7 = null
            0xa12d01d4 = null
            0xceea5b05 = null
            0x39a259d8 = null
            0xb1a12618 = null
            0xf67630ac = MapGroup {
                members: list2[string] = {
                    "723eff7d-aa4e-4373-9a9c-9cdd898aa6c2"
                    "20a2127a-1d5e-4292-aec4-a5fc2c1eca21"
                    "8d15b268-304b-44c5-a721-f189910449fd"
                    "fc723798-16ab-4980-bd12-439ddae08168"
                    "c889ecae-0b25-4119-a730-c6fd0e2e5c5b"
                    "83bc6a4c-fd6b-4fb4-88c3-40430da555ad"
                    "580b45eb-942f-4a26-bcf9-e3f218e311d5"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    1973.49194, -345.76239, 2943.51978, 1
                }
                name: string = "group1"
            }
            0x44d66d69 = null
            0xf9572089 = MapGroup {
                members: list2[string] = {
                    "3bea3f48-d63e-42de-886d-162486a809e5"
                    "53936940-3855-4245-af82-2b3615d85829"
                    "f8183051-8ce9-42bf-b0d4-1c0f585d94fc"
                    "d04ec4b2-6158-48fc-9158-e230cc9f4a51"
                    "df3a7a31-2d13-443c-8497-aaaf54953fb1"
                    "98a24e1f-9eaa-415b-8e96-2944d5259ccb"
                    "54170a2a-5d64-4920-b6d0-a2c92153bebf"
                    "bae36f11-fb8e-49df-bf4e-73b0a4c1ff8d"
                    "d75b4d7a-25c2-4c72-9da3-925f784e4cfa"
                    "8d40db2d-abe4-4ae0-81a7-bb03c871f888"
                    "94b670bc-a7ea-4b51-8ef5-ebc5d9d5abb7"
                    "83a9864b-706e-4fbb-b18c-93cf3ef1a556"
                    "f4bce724-7a45-40fa-842b-b950f34d56c7"
                }
                transform: mtx44 = {
                    1.54689968, 0, 0, 0
                    0, 1.54689968, 0, 0
                    0, 0, 1.54689968, 0
                    1267.82617, -231.649445, 565.045898, 1
                }
                name: string = "group2"
            }
            0x079093a0 = MapGroup {
                members: list2[string] = {
                    "621d4c65-885d-4fe4-b946-b59fba8838c9"
                }
                transform: mtx44 = {
                    1.29129589, 0, 0, 0
                    0, 1.29129589, 0, 0
                    0, 0, 1.29129589, 0
                    2872.72852, -238.80069, -236.790039, 1
                }
                name: string = "group3"
            }
            0x1f993661 = null
            0x8531389d = null
            0x16af983e = null
            0xaa29a82d = null
            0xaa9f245c = null
            0x52ef315e = null
            0xd97e7509 = null
            0x9b099529 = MapGroup {
                members: list2[string] = {
                    "da17f72f-43a3-45af-ace9-38276f663845"
                    "033c940b-fbca-42d7-b1e9-c2ed6d76b974"
                    "1cfe23ad-6041-4f83-b94d-d95c451a5c42"
                    "df4d7e60-4f73-4f2f-8a4f-b383984baa43"
                    "521328eb-7ddc-46b0-9406-b602dab42ae9"
                    "45763b3b-5b88-4b99-8a8b-160c3d9662e7"
                }
                transform: mtx44 = {
                    0.924084485, 0, 0, 0
                    0, 0.924084485, 0, 0
                    0, 0, 0.924084485, 0
                    2708.18335, -215.500641, 1157.73132, 1
                }
                name: string = "group4"
            }
            0xb3b9ba8e = null
            0x2b7d3a10 = null
            0xdbc99122 = null
            0x4ff3abaf = null
            0xa23947c1 = null
            0x68b4a5cb = MapGroup {
                members: list2[string] = {
                    "1917fca9-11ff-48b8-9400-71cafb7ae615"
                    "00d3aaf7-2dda-4031-824a-d6f440ce71ae"
                    "bf938534-99f3-4bb4-9c03-2471e64b364a"
                    "71c6b9ef-4ddb-4992-9495-5d3ccac07996"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    2915.84644, -4.94253159, 2674.65503, 1
                }
                name: string = "group5"
            }
            0x85826be6 = null
            0xbff72281 = null
            0x98ae71cd = null
            0x78134dae = null
            0xfdead521 = null
            0x9037852a = null
            0xc2e15b3f = MapGroup {
                members: list2[string] = {
                    "3522c077-3d5a-4002-9b57-32587568e61b"
                    "8171c8fb-96ad-4c6a-a383-c07743d208c9"
                    "7eb69bc4-cd79-4c04-ade6-00d38d92b8e1"
                    "16bd2f5c-ad03-45d1-a5e7-a84c07941e10"
                    "f031cacc-f0a3-44af-aa7d-4c4ea4b24666"
                    "a8898dd1-5029-4883-a177-4a8dc3bea187"
                    "b386c36a-bee8-4889-a289-1c17f5e565ec"
                    "5590a764-544a-43bf-988c-021130089a69"
                    "8d815490-40bc-4cf4-9501-565f5eebcb36"
                    "98d7dea8-3ebe-4f4b-9396-46446d5fa3ad"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    2212.23877, -216.785004, 2894.87183, 1
                }
                name: string = "group6"
            }
            0x7e36abdb = null
            0x76a91c0f = null
            0x0adb3f61 = null
            0x0ad96c49 = MapGroup {
                members: list2[string] = {
                    "ea31d25a-dbf6-4c89-983a-2486b829ed1a"
                }
                transform: mtx44 = {
                    0.999523878, 0.00158235326, -0.0308141708, 0
                    0, 0.998684108, 0.0512839071, 0
                    0.0308547728, -0.0512594916, 0.998208642, 0
                    209.867401, 189.048141, 2213.03808, 1
                }
                name: string = "group7"
            }
            0xce247a53 = null
            0xe08948e2 = null
            0xa1e7c4ec = null
            0x4be17479 = null
            0xbbe4cd93 = null
            0xa70c9b0e = null
            0x46f47c57 = null
            0x57282f37 = null
            0x5c5379f5 = null
            0xa6669765 = null
            0xc455852a = null
            0x6c87efdc = null
            0xe3cedff8 = null
            0x110233ca = null
            0x16c7e698 = null
            0xfd9e98f6 = null
            0x205f49a4 = null
            0x677cfb84 = null
            0x1501c66c = null
            0xdd75cee6 = null
            0x4f9ec9cc = null
            0x625283d8 = null
            0x4dada11b = null
            0xbd252eb1 = null
            0x1c0eaa0d = null
            0xfef0c8c8 = null
            0xb8aab8b5 = MapGroup {
                members: list2[string] = {
                    "7b829a44-ad5a-46ef-9c9e-0afa64beee7c"
                    "2559aea0-fe0b-4145-9f3f-8f8dfe8eeeb5"
                    "358a033b-9cb3-4565-a702-3d88f9bf81ce"
                    "182126aa-6315-4740-a5c1-5b53baa27e19"
                    "61e0f57f-1dd6-4879-9634-446b7c6f3d22"
                    "ca50fa75-a981-49ec-8c26-a70284459c2b"
                    "f24b54b6-c0e6-44e8-b374-51244aee6838"
                    "31b779e5-c4e7-4658-bbeb-96b118e95b9a"
                    "88e8490f-2976-4f87-b808-50d7d9b627f9"
                    "f77ac073-3977-41fe-b196-22928421b744"
                }
                transform: mtx44 = {
                    -0.763346612, 0, 0.374839753, 0
                    0, 0.408718467, 0, 0
                    -0.374839753, 0, -0.763346612, 0
                    2994.04761, 4.64550781, 1979.59473, 1
                }
                name: string = "group11"
            }
            0x2f00b8e3 = null
            0x0f891c5b = null
            0x776ce47a = null
            0x47266367 = null
            0xb17c2e89 = null
            0x1d460003 = null
            0xe2d45264 = MapGroup {
                transform: mtx44 = {
                    0.832868516, -0.106509216, 0, 0
                    0.106509216, 0.832868516, 0, 0
                    0, 0, 0.839651227, 0
                    3277.47974, -915.530396, 1259.97485, 1
                }
                name: string = "group9"
            }
            0x6bda4dd2 = null
            0x93c158b0 = null
            0x0777dee5 = null
            0x105d935d = null
            0x8ea8fca7 = null
            0x207c3b7f = null
            0x4122bcc6 = null
            0xa83313e5 = null
            0x8ccde282 = null
            0x28d9f19e = null
            0x2f7592b3 = null
            0x04755069 = null
            0xcbd5fba3 = null
            0x48fc282d = null
            0x977064db = null
            0x15b144e4 = null
            0x1c1ea5c6 = null
            0xdf16ef03 = MapGroup {
                members: list2[string] = {
                    "5a56e3be-77cf-4e52-8b30-679bf0d90fc5"
                    "efe6d728-a72e-41d9-bfb0-70b4b7e5020f"
                    "7e7d5174-af6f-4528-8e68-d6ba1230952a"
                    "bf0bdfc2-f3dd-4672-81ee-22b5dbd69a34"
                    "3dfc28d0-8684-47b9-92ad-ce38d7d43411"
                    "d3a84ae7-390c-4c89-b767-25181719d730"
                    "99e54a2a-4a87-46a4-bdd3-73d0a1bc1ed0"
                    "2431eb24-8862-4fc3-975d-0d54a4179dfa"
                    "f671b5fb-902b-417c-a58b-9410265d1908"
                    "778196b3-ecc5-4fd9-bfed-84db1176abe1"
                    "38740d39-9c0a-4d44-8b90-100f0514e910"
                    "191214e9-1442-4b3d-bbf8-3d48f29474c9"
                    "80a56327-467c-4fe1-a6cc-b0630f8daec9"
                    "b48416bf-893a-470e-ae6e-dc94277e01c7"
                }
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 0.695770562, 0, 0
                    0, 0, 1, 0
                    2972.23999, -10.3143969, 1814.87097, 1
                }
                name: string = "group13"
            }
            0x315863bf = MapGroup {
                transform: mtx44 = {
                    0.911049664, 0, 0, 0
                    0, 0.911049664, 0, 0
                    0, 0, 0.911049664, 0
                    3892.62378, -881.382751, 2275.3916, 1
                }
                name: string = "group14"
            }
            0x10ad3130 = null
            0xf8801cfc = null
            0x4101c4e0 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/Audio_Celestial" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x35387d16 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1801.38965, 259.48645, 2416.89478, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Amb_Loop1"
            }
            0xdadc63d6 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Arps"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1974.63501, 232.204041, 2423.9248, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Arps1"
            }
            0x3d3343fd = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Glassy_Wisps"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2134.98047, 317.009399, 2363.95825, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Twinkles1"
            }
            0xf0aefb4a = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Rumble"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    35413.7578, 0, 839408.75, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Rumble1"
            }
            0x8df848e9 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Rumble"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1843.24634, 328.050629, 1640.39233, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Rumble3"
            }
            0xd7bfaf12 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Tones"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1872.12671, 400.866821, 1994.41235, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Tones1"
            }
            0x41a939b6 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1857.27856, 274.132874, 2082.4209, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Wind1"
            }
            0xea8fae5a = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Flute"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1507.61792, 0, 894.753784, 1
                }
                name: string = "TFT_Audio-Emitter_DarkStar_Celestial_Cosmic_Flute1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/Audio_Celestial"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/VFX_Celestial" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x1ec98f75 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Large_Burning_Hair_Celestial"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    531, 355, 2639, 1
                }
                name: string = "Large_Burning_Hair_Celestial1"
            }
            0x6d6927ab = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
                transform: mtx44 = {
                    0.754857779, 0, -0.655888498, 0
                    0, 1, 0, 0
                    0.655888498, 0, 0.754857779, 0
                    1040.27417, 0.000122070312, 910.657959, 1
                }
                name: string = "Northern_Lights_Celestial1"
            }
            0xd07bda33 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
                transform: mtx44 = {
                    0.776417494, 0, 0.914973021, 0
                    0, 1.20000005, 0, 0
                    -0.914973021, 0, 0.776417494, 0
                    2861.91724, -141.992691, 1038.6001, 1
                }
                name: string = "Northern_Lights_Celestial2"
            }
            0x032e86d8 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
                transform: mtx44 = {
                    0.720674455, 0, -0.693273664, 0
                    0, 1, 0, 0
                    0.693273664, 0, 0.720674455, 0
                    3205.95605, -248.906433, 3332.0769, 1
                }
                name: string = "Northern_Lights_Celestial3"
            }
            0x2271dec2 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
                transform: mtx44 = {
                    0.962851644, 0, -0.270030797, 0
                    0, 1, 0, 0
                    0.270030797, 0, 0.962851644, 0
                    1359.27075, -98.4875488, 3550.54077, 1
                }
                name: string = "Northern_Lights_Celestial4"
            }
            0xfd911a1f = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/DarkStar_Eyes_Celestial"
                transform: mtx44 = {
                    0.911893964, -0.0829888508, -0.401947767, 0
                    -0.120287634, 0.882298589, -0.455060422, 0
                    0.392402887, 0.463316292, 0.794580281, 0
                    772.532654, 378.510956, 2576.95654, 1
                }
                name: string = "DarkStar_Eyes_Celestial2"
            }
            0xaef4d4d9 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/DarkStar_Eyes_Celestial"
                transform: mtx44 = {
                    0.116008684, -0.18070206, -0.976672292, 0
                    -0.443002611, 0.870675981, -0.213710457, 0
                    0.888982952, 0.457460582, 0.0209544878, 0
                    605.895142, 221.515411, 2491.58716, 1
                }
                name: string = "DarkStar_Eyes_Celestial3"
            }
            0x9d90a724 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_DarkStar_Celestial_Burning_Neck"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1264.89697, 42.5991821, 2445.56665, 1
                }
                name: string = "TFT_DarkStar_Celestial_Burning_Neck"
            }
            0xaa0c3a81 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/Northern_Lights_Celestial"
                transform: mtx44 = {
                    -0.0405398607, 0, -0.999178052, 0
                    0, 1, 0, 0
                    0.999178052, 0, -0.0405398607, 0
                    3475.48291, -203.180237, 2144.82251, 1
                }
                name: string = "Northern_Lights_Celestial5"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/VFX_Celestial"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Celestial" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2ada5579 = null
            0xc9e06b1d = null
            0x3a498c01 = null
            0x3363d89e = null
            0x1b3c6b1f = null
            0xbfeb65d4 = null
            0x2778d31a = null
            0x9d6d08ca = null
            0x0b09d0c2 = null
            0x291bef67 = null
            0x3891f86e = null
            0x8f70fd9c = null
            0x4ba36a79 = null
            0x93ba9fcc = null
            0x6dbbb742 = null
            0x8a281275 = null
            0xcacd5787 = MapParticle {
                system: link = "Maps/Particles/TFT/DarkStar/Celestial/TFT_Skybox_Darkstar_B"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 0, 2000, 1
                }
                name: string = "TFT_Skybox_Darkstar_B1"
                0xccf79327: u8 = 126
            }
            0xca403a5c = null
            0x6631c2c7 = null
            0x60ef92d5 = null
            0x033b44e5 = null
            0x8eb4c4aa = null
            0x918c10c4 = null
            0x014ba657 = null
            0xeaa820cd = null
            0x8fb03f43 = null
            0x5f3eb289 = null
            0x41f7899f = null
            0xbcc3c13d = null
            0x469483e8 = null
            0xa3cf3df1 = null
            0x1ed76b5d = null
            0x3a31c221 = null
            0xbe9e5907 = null
            0xa675267d = null
            0xbc82bede = null
            0x20fe82f0 = null
            0x8cc4acfb = null
            0x92787b3f = null
            0xc0e20b74 = null
            0xf9959d73 = null
            0x3e49b5c3 = null
            0xaad2a979 = null
            0x78d637c8 = null
            0xbc8cf83c = null
            0xbfe68b3d = null
            0xf165efb4 = null
            0x53436e70 = null
            0xa90e82d5 = null
            0x77d89bb6 = null
            0x66763f5a = null
            0x9efb2634 = null
            0x10daf841 = null
            0xd5502d74 = null
            0x549ecb23 = null
            0xa581b78d = null
            0x6544b6d2 = null
            0x4a285c25 = null
            0x4de1b025 = null
            0x90d6c604 = null
            0xd94caac6 = null
            0x4a79e911 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Celestial"
    }
    "Maps/MapGeometry/Map22/Chunks/Darkstar/LightingVolume_Celestial" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xd58dd7a0 = MapLightingVolume {
                sunColor: vec4 = { 0.62999922, 0.600000024, 0.689997733, 1 }
                sunDirection: vec3 = { 4, 5, -3 }
                0xd8851203: f32 = 500
                0xba02f116: f32 = 0.400000006
                skyLightColor: vec4 = { 0.345098048, 0.580392182, 0.529411793, 1 }
                horizonColor: vec4 = { 0.741176486, 0.768627465, 0.952941179, 1 }
                groundColor: vec4 = { 0.345098048, 0.592156887, 0.619607866, 1 }
                skyLightScale: f32 = 0.400000006
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.117647059, 0.137254909, 0.196078435, 1 }
                fogAlternateColor: vec4 = { 0.145098045, 0.349019617, 0.564705908, 1 }
                fogStartAndEnd: vec2 = { 500, -650 }
                transform: mtx44 = {
                    2300, 0, 0, 0
                    0, 3500, 0, 0
                    0, 0, 2500, 0
                    2000, 0.527008057, 2006.77124, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Darkstar/LightingVolume_Celestial"
    }
    "Maps/MapGeometry/Map22/Darkstar_Celestial" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Darkstar_Celestial"
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
                0x22d24a9a: f32 = 0.899999976
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Darkstar_Celestial/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Darkstar_Celestial_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0x26080855 = "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Shared"
            0x793a8d17 = "Maps/MapGeometry/Map22/Chunks/Darkstar/Lighting_Celestial"
            0xdd4dff0d = "Maps/MapGeometry/Map22/Chunks/Darkstar/Audio_Celestial"
            0x2abc7ab6 = "Maps/MapGeometry/Map22/Chunks/Darkstar/Art_Celestial"
            0x94d15edf = "Maps/MapGeometry/Map22/Chunks/Darkstar/VFX_Celestial"
            0x9785afed = "Maps/MapGeometry/Map22/Chunks/Darkstar/LightingVolume_Celestial"
            "Darkstar_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Darkstar/Darkstar_Design_Base"
        }
    }
    0x4ddca076 = MapPointLightType {
        radius: f32 = 800
        Impact: i32 = 1
    }
    0x7ca5e4f1 = MapPointLightType {
        lightColor: vec4 = { 0.105882354, 0.321568638, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x925f06fe = MapPointLightType {
        lightColor: vec4 = { 0.564705908, 0.490196079, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xdc31003a = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.717647076, 0.823529422, 1 }
    }
}
