#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Brazier_Base_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Brazier_Base_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Brazier_Base_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Doorway_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Doorway_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Doorway_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Opponent_Side_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Keystone_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Keystone_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Keystone_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Bench_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Bench_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Bench_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Opponent_Side_B.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Column_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Column_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Column_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Bottom_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Bottom_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/TFT_Freljord_Skybox_Bottom.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Wood_Beam_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Wood_Beam_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Wood_Beam_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Flag_Stand_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Flag_Stand_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flag_Stand_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Statue_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Statue_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Statue_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Bridge_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Bridge_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Bridge_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Small_Props_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Small_Props_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Small_Props_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Staircase_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Staircase_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Staircase_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Black_Ice_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Black_Ice_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Black_Ice_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Fortress_B.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Side_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Side_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/TFT_Freljord_Skybox_Side.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Glaciers_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Glaciers_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Glaciers_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Fortress_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Chain_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Chain_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Chain_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Snow_Banks_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Snow_Banks_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Snow_Banks_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Flags_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Flags_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flags_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/SnowIcicles_Alphas_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/SnowIcicles_Alphas_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/SnowIcicles_Alphas_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_Statue_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_Statue_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Banners_A.TFT_Freljord.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Y_Axis"
                value: vec4 = { -1, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Frequency"
                value: vec4 = { 4, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Low"
                value: vec4 = { -1.26999998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_High"
                value: vec4 = { 1.40999997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Vertex_Displacement"
                value: vec4 = { 0, -2, -4, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Z_Axis"
                value: vec4 = { -0.600000024, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Frequency"
                value: vec4 = { 15, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Low"
                value: vec4 = { -2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_High"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Vertex_Displacement"
                value: vec4 = { -8, -17, 0.75, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_X_Axis"
                value: vec4 = { -0.400000006, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Frequency"
                value: vec4 = { 12, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Low"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Vertex_Displacement"
                value: vec4 = { 10, 2, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Rotation"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Rotation"
                value: vec4 = { 74.6999969, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Rotation"
            }
            StaticMaterialShaderParamDef {
                name: string = "X_UV_Mask_Distance_Offset"
                value: vec4 = { -0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_Low"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_UV_Mask_Distance_Offset"
                value: vec4 = { -0.0599999987, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_Low"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_UV_Mask_Distance_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_Low"
                value: vec4 = { 0.00999999978, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_High"
                value: vec4 = { 0.639999986, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Global_Intensity"
                value: vec4 = { 2, 1, 120, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Offset_UV_Wave"
                value: vec4 = { 1, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
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
                name: string = "Y_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_X_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Y_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Z_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_REMOVE_ALPHA"
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
                        shader: link = "Shaders/StaticMesh/TFT_VertexWave"
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
                    name: string = "Wind_Global_Intensity"
                    enabled: bool = false
                    driver: pointer = TimeMaterialDriver {}
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flags_A.TFT_Freljord.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Y_Axis"
                value: vec4 = { -1, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Frequency"
                value: vec4 = { 4.4000001, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Low"
                value: vec4 = { -1.26999998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_High"
                value: vec4 = { 1.40999997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Vertex_Displacement"
                value: vec4 = { 0, -6, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Z_Axis"
                value: vec4 = { -0.600000024, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Frequency"
                value: vec4 = { 10, 0.850000024, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Low"
                value: vec4 = { -2.81999993, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_High"
                value: vec4 = { 2.80999994, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Vertex_Displacement"
                value: vec4 = { -8, -19, 0.75, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_X_Axis"
                value: vec4 = { -0.810000002, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Frequency"
                value: vec4 = { 3.70000005, 0.550000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Low"
                value: vec4 = { -2.11999989, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_High"
                value: vec4 = { 1.38999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Vertex_Displacement"
                value: vec4 = { 20, 50, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Rotation"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Rotation"
                value: vec4 = { 2.9000001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Rotation"
                value: vec4 = { 3.1400001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_UV_Mask_Distance_Offset"
                value: vec4 = { -0.219999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_Low"
                value: vec4 = { 0.25, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_UV_Mask_Distance_Offset"
                value: vec4 = { -0.0599999987, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_Low"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_UV_Mask_Distance_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_Low"
                value: vec4 = { 0.00999999978, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_High"
                value: vec4 = { 0.639999986, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Global_Intensity"
                value: vec4 = { 1, 0.5, 120, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Offset_UV_Wave"
                value: vec4 = { 1, 0.800000012, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Offset_UV_Wave"
                value: vec4 = { 5.19999981, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
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
                name: string = "Y_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_X_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Y_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Z_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_REMOVE_ALPHA"
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
                        shader: link = "Shaders/StaticMesh/TFT_VertexWave"
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
                    name: string = "Wind_Global_Intensity"
                    enabled: bool = false
                    driver: pointer = TimeMaterialDriver {}
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_Frostguard_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_Frostguard_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_C.TFT_Freljord.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_C_Mask.TFT_Freljord.dds"
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
                value: vec4 = { 0.600000024, 0.220004573, 0.379995435, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Bounds"
                value: vec4 = { 0, 0.600000024, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Frequency"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Speed"
                value: vec4 = { 40, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { -2, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Frequency"
                value: vec4 = { 1.79999995, 0, 0, 0 }
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
                value: vec4 = { 0.5, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity_Min_Max"
                value: vec4 = { 0.100000001, 1, 0, 0 }
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
            }
            StaticMaterialSwitchDef {
                name: string = "RADIAL_UV_LOCALSPACE_TOGGLE"
            }
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
    }
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_Brazier_2.dds"
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
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Chain_Movement" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Chain_Movement"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Chain_Movement"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_chain_movement"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard_Muted" = VfxSystemDefinitionData {
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
                    constantValue: vec3 = { 500, 750, 0 }
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
                            { 500, 750, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 15, 15 }
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
                                { 15, 15, 15 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.509803951, 0.447058827, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.509803951, 0.447058827, 0 }
                            { 1, 0.509803951, 0.447058827, 1 }
                            { 1, 0.509803951, 0.447058827, 0.800000012 }
                            { 1, 0, 0, 0 }
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
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
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
                            0.449999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 200 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
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
                            { 1, 1, 1, 0.800000012 }
                            { 0, 0, 0.498039216, 0 }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Dust_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
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
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.300007641, 0.590005338, 0.130006865, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
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
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
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
                            { 100, 100, 0 }
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
                    constantValue: vec4 = { 0.152941182, 0.20784314, 0.270588249, 0.631372571 }
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
                            { 0.152941182, 0.20784314, 0.270588249, 0.631372571 }
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
                            { 0.458823532, 0, 0, 0.239215687 }
                            { 0.992156863, 0, 0, 1 }
                            { 0.459998488, 0, 0, 0.450003803 }
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
                    constantValue: vec3 = { 80, 80, 0 }
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
                            { 80, 80, 0 }
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
                    constantValue: f32 = 2
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
                            2
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
                emitterName: string = "baseGlow"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.701960802, 0.333333343, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.701960802, 0.333333343, 0 }
                            { 1, 0.701960802, 0.333333343, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Varus/Skins/Base/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
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
                emitterName: string = "baseGlow1"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
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
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
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
                emitterName: string = "baseGlow2"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
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
                pass: i16 = 50
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
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
                    10.1999998
                }
                emitterName: string = "ground_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.710002303, 0.130006865, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.710002303, 0.130006865, 1, 0 }
                            { 0.710002303, 0.130006865, 1, 0.800000012 }
                            { 0.710002303, 0.130006865, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
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
                            { 150, 340, 340 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                emitterName: string = "mouth_flame_R"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 45, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 15, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
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
                pass: i16 = -2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 2 }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 50 }
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
                            { 70, 70, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
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
                    constantValue: f32 = 0.800000012
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
                            0.800000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks1"
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
                    constantValue: vec3 = { 300, 100, 300 }
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
                            { 300, 100, 300 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588237, 0.709803939, 1, 1 }
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
                            { 1, 0, 0, 0 }
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
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "TFT_Freljord_BrazierFire_FrostGuard_Muted"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard_Muted"
        flags: u8 = 197
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Air_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Air_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Air_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_air_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_wind_cold_gust"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Fire"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_fire_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Ice_Crumble" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Ice_Crumble"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Ice_Crumble"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_ice_crumble"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
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
                                    0.300000012
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
                childParticleSetDefinition: embed = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effect: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow_Child"
                        }
                    }
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
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
                emitterName: string = "brightSnow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, -150, 400 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, -150, 400 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1600, 1200 }
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
                                { 1200, 1600, 1200 }
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
                    constantValue: vec4 = { 0.779995441, 0.349996179, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.779995441, 0.349996179, 1, 0 }
                            { 0.779995441, 0.349996179, 1, 1 }
                            { 0.779995441, 0.349996179, 1, 0 }
                        }
                    }
                }
                pass: i16 = 200
                isDirectionOriented: flag = true
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Firefly_Mote.TFT_Set5.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
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
                                    0.300000012
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
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 30
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 100
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "darkSnow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, -300, 400 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, -300, 400 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1600, 1200 }
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
                                { 1200, 1600, 1200 }
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
                    constantValue: vec4 = { 0.78039217, 1, 0.305882365, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.78039217, 1, 0.305882365, 0 }
                            { 0.78039217, 1, 0.305882365, 1 }
                            { 0.78039217, 1, 0.305882365, 0 }
                        }
                    }
                }
                pass: i16 = 200
                isDirectionOriented: flag = true
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Firefly_Mote.TFT_Set5.dds"
                uvMode: u8 = 2
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Freljord_FrostGuard_Snow"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Groan_Distant" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Groan_Distant"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Groan_Distant"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_groan_distant"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
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
                            0.100000001
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
                                    0
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
                    0.200000003
                }
                emitterName: string = "brightSnow"
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
                    constantValue: vec4 = { 0.670588255, 0.819607854, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.670588255, 0.819607854, 1, 0 }
                            { 0.670588255, 0.819607854, 1, 1 }
                            { 0.670588255, 0.819607854, 1, 0 }
                        }
                    }
                }
                pass: i16 = 200
                isDirectionOriented: flag = true
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 16, 16, 0 }
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
                            { 16, 16, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/glowspecks.dds"
                uvMode: u8 = 2
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Freljord_FrostGuard_Snow_Child"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow_Child"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
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
                                    0.800000012
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
                    2
                }
                emitterName: string = "Wind"
                shape: embed = VfxShape {
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
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.7400015 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.56078434, 0.662745118, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.56078434, 0.662745118, 1, 0 }
                            { 0.56078434, 0.662745118, 1, 1 }
                            { 0.56078434, 0.662745118, 1, 1 }
                            { 0.56078434, 0.662745118, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.5
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
                                    10
                                    -10
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
                    constantValue: vec3 = { 20, 10, 10 }
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
                            { 20, 10, 10 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0799999982, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0799999982, 0 }
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
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
                            0.200000003
                        }
                    }
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
                                    0.800000012
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
                    2
                }
                emitterName: string = "WindDark"
                shape: embed = VfxShape {
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
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.730006874 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.730006874 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.710002303, 0.600000024, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.710002303, 0.600000024, 1, 0 }
                            { 0.710002303, 0.600000024, 1, 0.800000012 }
                            { 0.710002303, 0.600000024, 1, 0.800000012 }
                            { 0.710002303, 0.600000024, 1, 0 }
                        }
                    }
                }
                pass: i16 = 49
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 300
                }
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
                                    10
                                    -10
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
                    constantValue: vec3 = { 20, 10, 10 }
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
                            { 20, 10, 10 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0500000007, 0 }
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
            }
        }
        visibilityRadius: f32 = 8000
        particleName: string = "TFT_Freljord_FrostGuard_Edge_Fog"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Wind" = VfxSystemDefinitionData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                    constantValue: vec4 = { 0.910002291, 0.379995435, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.910002291, 0.379995435, 1, 0 }
                            { 0.910002291, 0.379995435, 1, 1 }
                            { 0.910002291, 0.379995435, 1, 0 }
                        }
                    }
                }
                pass: i16 = 60
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
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
        particleName: string = "TFT_Freljord_FrostGuard_Wind"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Wind"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard" = VfxSystemDefinitionData {
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
                    constantValue: vec3 = { 500, 750, 0 }
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
                            { 500, 750, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 15, 15 }
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
                                { 15, 15, 15 }
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
                    constantValue: vec4 = { 1, 0.278431386, 0.184313729, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.278431386, 0.184313729, 0 }
                            { 1, 0.278431386, 0.184313729, 1 }
                            { 1, 0.278431386, 0.184313729, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
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
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
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
                            0.449999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 200 }
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
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Dust_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
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
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0.300007641, 0.590005338, 0.130006865, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
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
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
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
                            { 100, 100, 0 }
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
                    constantValue: vec4 = { 0.269993126, 0.269993126, 0.269993126, 0.62999922 }
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
                            { 0.269993126, 0.269993126, 0.269993126, 0.62999922 }
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
                            { 0.458823532, 0, 0, 0.239215687 }
                            { 0.992156863, 0, 0, 1 }
                            { 0.459998488, 0, 0, 0.450003803 }
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
                    constantValue: vec3 = { 80, 80, 0 }
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
                            { 80, 80, 0 }
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
                    constantValue: f32 = 2
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
                            2
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
                emitterName: string = "baseGlow"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.701960802, 0.333333343, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.701960802, 0.333333343, 0 }
                            { 1, 0.701960802, 0.333333343, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Varus/Skins/Base/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
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
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
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
                emitterName: string = "baseGlow2"
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
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
                    10.1999998
                }
                emitterName: string = "ground_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.710002303, 0.130006865, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.710002303, 0.130006865, 1, 0 }
                            { 0.710002303, 0.130006865, 1, 0.800000012 }
                            { 0.710002303, 0.130006865, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
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
                            { 150, 340, 340 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                emitterName: string = "mouth_flame_R"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 45, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 15, 0 }
                    }
                }
                blendMode: u8 = 1
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
                pass: i16 = -2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 2 }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 50 }
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
                            { 70, 70, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Maps/Particles/TFT/TFT_Glb_Gradient.TFT_Set5.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 8, 0, 0 }
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
                    constantValue: f32 = 0.800000012
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
                            0.800000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks1"
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
                    constantValue: vec3 = { 300, 100, 300 }
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
                            { 300, 100, 300 }
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
                            { 1, 0, 0, 0 }
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
                        constantValue: vec3 = { 8, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "TFT_Freljord_BrazierFire_FrostGuard"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard"
        flags: u8 = 197
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Fog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                                    0.800000012
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
                    2
                }
                emitterName: string = "Wind"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 4000 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -500
                                        0
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
                            values: list[vec3] = {
                                { 0, 1, 4000 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
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
                    constantValue: vec4 = { 0.56078434, 0.662745118, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.56078434, 0.662745118, 1, 0 }
                            { 0.56078434, 0.662745118, 1, 1 }
                            { 0.56078434, 0.662745118, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 1000
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 80, 80 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 80, 80 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0149999997, 0 }
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
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
                                    0.800000012
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
                    2
                }
                emitterName: string = "WindDark"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -200, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 4000 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -500
                                        0
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
                            values: list[vec3] = {
                                { 0, 1, 4000 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.709803939, 0.596078455, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.709803939, 0.596078455, 1, 0 }
                            { 0.709803939, 0.596078455, 1, 1 }
                            { 0.709803939, 0.596078455, 1, 1 }
                            { 0.709803939, 0.596078455, 1, 0 }
                        }
                    }
                }
                pass: i16 = 49
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 800
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 80, 80 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 80, 80 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0149999997, 0 }
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
            }
        }
        visibilityRadius: f32 = 8000
        particleName: string = "TFT_Freljord_FrostGuard_Fog"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Fog"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Whispers" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Whispers"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Whispers"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_whispers"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Void_Rumble" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Frostguard_Void_Rumble"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Void_Rumble"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_frostguard_void_rumble"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Godrays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    17
                }
                emitterName: string = "Godray"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 900, 0, 1 }
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
                                { 900, 0, 1 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Godrays_Mesh.TFT_Freljord.scb"
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
                            { 0.470588237, 0.949019611, 1, 0 }
                            { 0.411764711, 0.717647076, 1, 1 }
                            { 0.325490206, 0.41568628, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
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
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_GodRays.TFT_Freljord.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
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
                                    0
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
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "GodrayBright"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 600 }
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
                                { 600, 0, 600 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_GodRay.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.513725519, 0.847058833, 1 }
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
                pass: i16 = 100
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_GodRays.TFT_Freljord.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
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
                                    0
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
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "GodrayDark"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 600 }
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
                                { 600, 0, 600 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_GodRay.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.164705887, 0.113725491, 0.223529413, 1 }
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
                pass: i16 = 100
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_GodRays.TFT_Freljord.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
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
                                    0
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
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Freljord_FrostGuard_Godrays"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Godrays"
        flags: u8 = 132
    }
    0x17bdecb5 = MapPointLightType {
        lightColor: vec4 = { 0.686274529, 0.36470589, 0.611764729, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
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
    0xae60cac5 = MapPointLightType {
        lightColor: vec4 = { 0.717647076, 0.211764708, 0.329411775, 1 }
        radius: f32 = 497
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xe753711c = MapPointLightType {
        lightColor: vec4 = { 0.34117648, 0.56078434, 0.607843161, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
    }
    0xfd78c09d = MapPointLightType {
        lightColor: vec4 = { 0, 0.172549024, 0.384313732, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
    }
    0xd14201ac = MapPointLightType {
        lightColor: vec4 = { 0.0274509825, 0.36470589, 0.870588303, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Frostguard" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x7ea5a5bd = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Air_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1987.70178, -0.0009765625, 1975.55518, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Air_Loop1"
            }
            0x9bc53b8a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3283.75684, 0, 1909.39282, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust1"
            }
            0x79f1fb96 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    837.181519, 500.722778, 1942.92188, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Wind_Cold_Gust2"
            }
            0x1212dc5a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Ice_Crumble"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    759.910767, 346.340576, 1824.68579, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Ice_Crumble1"
            }
            0x194d26b3 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Void_Rumble"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1701.08997, -0.000518798828, 2025.07349, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Void_Rumble1"
            }
            0xa416ce29 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Groan_Distant"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2363.7439, -0.00146484375, 2006.09302, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Groan_Distant1"
            }
            0xd198cbb4 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Chain_Movement"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3297.50098, 355.246826, 1852.15356, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Chain_Movement1"
            }
            0x3b38ab83 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Whispers"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2117.62036, 266.459473, 1995.3833, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Whispers1"
            }
            0x88c89c6f = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1026.32898, 308, 931.895996, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Fire1"
            }
            0xcb180e52 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.46899, 308, 929.658997, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Fire2"
            }
            0xd0eadfe3 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2978.3689, 308, 3028.32007, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Fire3"
            }
            0xab737ef5 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Frostguard_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1027.77795, 308, 3024.31909, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Frostguard_Fire4"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Frostguard"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Frostguard" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x040f804d = null
            0x40725843 = null
            0x8b8ebe33 = null
            0xbf90adcd = null
            0x2215e6e0 = null
            0x35b65b4a = null
            0xe788c00c = null
            0xca6ab0dd = null
            0xd400dc7b = null
            0x4dd75902 = null
            0xe3788136 = null
            0x796d2ad8 = null
            0x396fd734 = null
            0x3973eb2e = null
            0xfb210a39 = null
            0xf85eccc1 = null
            0xec1462de = null
            0x98aeed9a = null
            0xffc9d36b = null
            0xc142e495 = null
            0x5a5bed05 = null
            0x44bcb4c3 = null
            0xab636c85 = null
            0x547b11cb = null
            0x25c5b33b = null
            0x077a5b48 = null
            0x14662880 = null
            0x4bca1d20 = null
            0x9a33e0f2 = null
            0xc56f0139 = null
            0xdae278af = null
            0xf8ddb4b8 = null
            0x969b45b5 = null
            0x4a002b64 = null
            0x3361857f = null
            0x23862676 = null
            0x70e6cab8 = null
            0xeeee8c8c = null
            0x18ac9fdf = null
            0x535c509a = null
            0x3d2c7a2b = null
            0xa0dcf17a = null
            0x6b1d0c16 = null
            0xd362af36 = null
            0xec7cbaf1 = null
            0xc80b2fc7 = null
            0x58954607 = null
            0x27a71195 = null
            0xdf7b5fbc = null
            0x35cfdea0 = null
            0x127e5850 = null
            0x7f1a6d3f = null
            0x065f499c = null
            0xa98a6978 = null
            0x71681f7f = null
            0x278fa888 = null
            0xb6b5f63e = null
            0x045c68dd = null
            0xc8549919 = null
            0xe38c68c2 = null
            0xc4f6dab2 = null
            0x07547a00 = null
            0xd9ff16f6 = null
            0xf97a8868 = null
            0x4fdecf9d = null
            0x10344d24 = null
            0x79c9804e = null
            0xdd8ffb96 = null
            0x959ee16c = null
            0xaf0fa714 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Frostguard"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Frostguard" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x660887c7 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.99999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3765.5581, -274.404907, 742.330078, 1
                }
                name: string = "Light_Blue1"
            }
            0x12190317 = MapPointLight {
                type: link = 0xd14201ac
                radiusScale: f32 = 1.49999619
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2025.87781, -846.201782, 1144.92163, 1
                }
                name: string = "Light_DarkBlue1"
            }
            0x8bfd0dd3 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3804.9187, -421.669159, 1428.18201, 1
                }
                name: string = "light_48_15"
            }
            0xc0a4fa40 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2976.33374, 331.612, 929.651733, 1
                }
                name: string = "light_23_1"
            }
            0xde488852 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1028.45862, 331.612, 929.651733, 1
                }
                name: string = "light_23_2"
            }
            0xc66ef5b7 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2976.33374, 331.612, 3025.96289, 1
                }
                name: string = "light_23_3"
            }
            0x24e034a7 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1028.45862, 331.612, 3025.96289, 1
                }
                name: string = "light_23_4"
            }
            0xfe32db25 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    410.928833, -273.486237, 2175.63428, 1
                }
                name: string = "light_23_5"
            }
            0x8a4eb16b = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3675.6936, -273.486237, 2180.45728, 1
                }
                name: string = "light_23_6"
            }
            0x19d7efea = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3149.23438, 61.7082825, 1942.93604, 1
                }
                name: string = "light_61_1"
            }
            0xb1e51b57 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.199999958
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    673.800354, -42.8981285, 1836.29163, 1
                }
                name: string = "light_9_1"
            }
            0xce23f67c = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.682793677
                intensityScale: f32 = 2.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1067.32715, 327.87262, 1467.34412, 1
                }
                name: string = "light_61_2"
            }
            0xebc8b7ba = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    662.392456, 27.0717964, 1614.24255, 1
                }
                name: string = "light_9_2"
            }
            0x313636cc = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3374.27148, -77.549057, 2101.46802, 1
                }
                name: string = "light_9_3"
            }
            0x7113a5cd = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3249.32593, -58.0426865, 1887.14404, 1
                }
                name: string = "light_38_3"
            }
            0xb3d622a3 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.36701113
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3471.35449, -290.636047, 1751.36255, 1
                }
                name: string = "light_61_3"
            }
            0x69717ca2 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3482.52881, -134.817154, 1624.51941, 1
                }
                name: string = "light_38_4"
            }
            0xce59c2a0 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3509.03418, -156.117432, 1724.68298, 1
                }
                name: string = "light_9_5"
            }
            0xfbfc99ab = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    747.262634, 84.1908875, 1315.81714, 1
                }
                name: string = "light_38_5"
            }
            0x34450b75 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    583.818909, -214.261887, 2155.48486, 1
                }
                name: string = "light_9_6"
            }
            0xefb5a1ea = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.75
                intensityScale: f32 = 2.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -131.716339, -833.895264, 2349.26758, 1
                }
                name: string = "light_38_7"
            }
            0x300ab3b3 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.199999958
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    303.130096, -354.858887, 1663.80396, 1
                }
                name: string = "light_9_7"
            }
            0xee57f8a7 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2742.92358, 75.4965668, 1409.02417, 1
                }
                name: string = "light_9_8"
            }
            0xca7ed7b2 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.341780275
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2761.99097, 156.686737, 774.303589, 1
                }
                name: string = "light_38_1"
            }
            0x8ab546fe = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3369.69189, 116.525764, 1133.42615, 1
                }
                name: string = "light_61_4"
            }
            0x243ee449 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1241.94263, 153.712463, 907.736755, 1
                }
                name: string = "light_38_9"
            }
            0x6515bcff = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    599.453186, 142.256531, 745.286316, 1
                }
                name: string = "light_38_10"
            }
            0x15f1a659 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2899.08496, 116.525764, 579.863647, 1
                }
                name: string = "light_61_5"
            }
            0x85fb340b = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2972.42334, 271.91629, 536.196411, 1
                }
                name: string = "light_38_11"
            }
            0x40103dbb = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3298.88867, 229.612305, 2832.96069, 1
                }
                name: string = "light_38_12"
            }
            0xf56b6621 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.5
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3461.948, 151.563782, 2924.47778, 1
                }
                name: string = "light_9_9"
            }
            0x591693bb = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2452.81299, 197.779541, 3439.97949, 1
                }
                name: string = "light_61_6"
            }
            0x0287e9c6 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1225.22412, 228.151581, 3513.39966, 1
                }
                name: string = "light_38_13"
            }
            0x6e3896ea = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    615.097839, 380.192902, 2918.77881, 1
                }
                name: string = "light_61_7"
            }
            0xa1c8417c = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1315.98901, 276.615692, 3652.66284, 1
                }
                name: string = "light_9_10"
            }
            0xdfb4bb46 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3883.72412, -399.892334, 2641.72632, 1
                }
                name: string = "Light_Blue2"
            }
            0xa632ad1c = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2988.21509, -260.914978, 294.318542, 1
                }
                name: string = "light_48_1"
            }
            0x88f72ac3 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1013.89941, -400.840088, 257.83313, 1
                }
                name: string = "Light_Blue3"
            }
            0x3dd984e7 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    236.74823, -260.914978, 1020.30975, 1
                }
                name: string = "light_48_2"
            }
            0xc35f3c05 = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    168.883789, -275.154633, 2810.13599, 1
                }
                name: string = "Light_Blue4"
            }
            0x72469c39 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    794.427612, -260.914978, 3717.23511, 1
                }
                name: string = "light_48_3"
            }
            0xaaabbc7a = MapPointLight {
                type: link = 0xe753711c
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2729.65771, 32.3227844, 3957.5542, 1
                }
                name: string = "Light_Blue5"
            }
            0xb9dbb216 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 1.49999976
                intensityScale: f32 = 3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.73242, -290.468048, 294.318542, 1
                }
                name: string = "light_48_4"
            }
            0xe749cf60 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 1.49999833
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -154.475891, -525.415527, 1924.60962, 1
                }
                name: string = "light_48_5"
            }
            0x328deeed = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 1.49999762
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4071.50903, -290.468048, 1924.60962, 1
                }
                name: string = "light_48_6"
            }
            0x030026a4 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    334.049683, -192.251175, 1779.32764, 1
                }
                name: string = "light_38_14"
            }
            0x1b8aaf4a = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.682793379
                intensityScale: f32 = 2.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2930.64648, 359.357941, 2491.51465, 1
                }
                name: string = "light_61_8"
            }
            0xb7909bf3 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    711.643005, 238.928558, 2740.4834, 1
                }
                name: string = "light_38_15"
            }
            0xbc70ca41 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    697.537842, 380.192993, 3132.22974, 1
                }
                name: string = "light_61_9"
            }
            0x258b0467 = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 1.2202003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1999.72205, 440.906799, 1999.88794, 1
                }
                name: string = "light_38_16"
            }
            0x8394411a = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.552444816
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1501.04358, 290.487305, 2243.41235, 1
                }
                name: string = "light_38_17"
            }
            0x917c57ad = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.551999986
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1501.04358, 290.487305, 1745.17285, 1
                }
                name: string = "light_38_18"
            }
            0x940b0ae3 = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.552444816
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2459.06226, 290.487305, 1745.17285, 1
                }
                name: string = "light_38_19"
            }
            0x1118123c = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.552444816
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2459.06226, 290.487305, 2243.41235, 1
                }
                name: string = "light_38_20"
            }
            0xe3e7bb61 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.336747229
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1165.13293, 138.553177, 3236.66846, 1
                }
                name: string = "light_38_21"
            }
            0xe20b5d02 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.336747229
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2796.9563, 88.6100922, 3051.94507, 1
                }
                name: string = "light_38_22"
            }
            0x978d682f = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 1.49999702
                intensityScale: f32 = 3
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3572.37695, -220.665009, 2026.31909, 1
                }
                name: string = "light_48_7"
            }
            0xcd0c8994 = MapPointLight {
                type: link = 0xfd78c09d
                radiusScale: f32 = 0.903670371
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    324.36319, -180.188248, 2020.59033, 1
                }
                name: string = "light_48_8"
            }
            0x35a5cbdf = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.341780275
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2761.99097, 156.686737, 879.303101, 1
                }
                name: string = "light_38_2"
            }
            0x1aa7b286 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1194.71448, 123.237335, 793.808716, 1
                }
                name: string = "light_38_6"
            }
            0x24bf911f = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.388067186
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1079.04578, 290.487305, 2227.67041, 1
                }
                name: string = "light_38_23"
            }
            0xa57a0f37 = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.552444816
                intensityScale: f32 = 0.300000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2981.27344, 290.487305, 1902.69604, 1
                }
                name: string = "light_38_24"
            }
            0x5859eafb = MapPointLight {
                type: link = 0x17bdecb5
                radiusScale: f32 = 0.388067186
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1079.04578, 290.487305, 1778.5061, 1
                }
                name: string = "light_38_8"
            }
            0x47c88552 = MapPointLight {
                type: link = 0x51710564
                radiusScale: f32 = 0.59709841
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1852.21106, 282.855011, 3314.10791, 1
                }
                name: string = "light_61_10"
            }
            0x84486a64 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    818.704102, 65.8070679, 1925.77454, 1
                }
                name: string = "light_38_25"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Frostguard"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x96cf3b17 = null
            0x8cdb744d = null
            0x185af8f1 = null
            0x7f04abf5 = null
            0xc53ce72c = null
            0x60f8df0b = MapGroup {
                members: list2[string] = {
                    "fa81f9f7-dae1-4efa-8fa4-38d81590378d"
                    "a727a693-7957-41e0-9445-c0c2a859738f"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3624.02661, -289.353882, 2712.75415, 1
                }
                name: string = "group1"
            }
            0x7c3a08ff = null
            0x017b3118 = null
            0x0f77f79e = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3897.4104, -1233.99731, 951.408203, 1
                }
                name: string = "group2"
            }
            0xd3c64d4c = null
            0x0c0c4621 = null
            0xc0a9295a = null
            0x842b30ce = null
            0x6dd2d5ea = null
            0x88f203dc = null
            0x6f594ec9 = null
            0xae96d0ba = null
            0x4b00daf5 = null
            0xb94027d1 = null
            0xecf2c869 = null
            0x1d1ca7fc = null
            0xd57b11a4 = null
            0xcbdbdbed = null
            0xd5dafdf1 = null
            0x06b3b399 = null
            0x0b05ad8d = null
            0x7b263331 = null
            0xb06f0919 = null
            0xb3ce48e0 = null
            0xa1e92f32 = null
            0xef28381a = null
            0x1677a040 = null
            0x62f75261 = null
            0xa3b715aa = null
            0x05448ec3 = null
            0xfda50dde = null
            0xdfe0551b = null
            0x9e7579da = null
            0xf6c9a647 = null
            0x3886890b = null
            0x7d3cdada = null
            0xee53c70a = null
            0x0d6c99f8 = null
            0x87c296bf = null
            0x1e87857e = null
            0x59b0217c = null
            0x2339622f = null
            0x042ec4ec = null
            0x2a6ecf92 = null
            0x11328b65 = null
            0xf6807de9 = null
            0xc7d71864 = null
            0xe95fafab = null
            0xf41cf36c = null
            0x57074043 = null
            0x5b5c1b1b = null
            0x2b655c22 = null
            0x64018cd4 = null
            0x61781b13 = null
            0x6198f647 = null
            0x31072a88 = null
            0x57321d2c = null
            0x0ac817ff = null
            0xba658b19 = null
            0xb0c9543d = null
            0x07c1b209 = null
            0x45aeaa4e = null
            0xb65ea301 = null
            0xcc7a56c5 = null
            0xcbdbc144 = null
            0x99acfc11 = null
            0xd1f683d5 = null
            0x300f1bb5 = null
            0x810f6bd2 = null
            0x88e05c9c = null
            0x466550f6 = null
            0xf7d7c608 = null
            0x3e9a0284 = null
            0x5f3d89f0 = null
            0x9e425297 = null
            0x7721da20 = null
            0x24b3a5af = null
            0x75b41dae = null
            0x6c17daec = null
            0x60f9bb2c = null
            0x39095c6f = null
            0x5a144719 = null
            0xd40caae1 = null
            0x783c1b36 = null
            0x2d79630b = null
            0x9257b4ed = null
            0xaaddf029 = null
            0xa0a8a3c3 = null
            0xe46fb61e = null
            0x41126533 = null
            0xa282ee9c = null
            0x43d01893 = null
            0x15240e4d = null
            0x5156372a = null
            0xd59bb555 = null
            0xe085e0cc = null
            0x532ab14e = null
            0xe1b4e328 = null
            0x93e26cee = null
            0xb9763556 = null
            0x63d1ca73 = null
            0x07f2951e = null
            0xe2074798 = null
            0xb5a8eb20 = null
            0xe33a3d85 = null
            0x7c79c110 = null
            0xf54ab6bc = null
            0x7611930f = null
            0x2b388211 = null
            0x8d6edcab = null
            0xc25581de = null
            0xb424065f = null
            0xfd117cfe = null
            0xd6e24041 = null
            0xf86f6bb5 = null
            0x0e2df091 = null
            0x5a70ff2c = null
            0x6bac4e6b = null
            0x49dd0f8c = null
            0x9adf1ecf = null
            0x7c6f44d6 = null
            0x7a234714 = null
            0xf839a9f9 = null
            0x316bbd34 = null
            0xf25d3250 = null
            0x0633f04a = null
            0x48c425f2 = null
            0x02e881dc = null
            0x99dafaac = null
            0xf5fcd608 = null
            0xe2acdeb1 = null
            0xd39f9ecc = null
            0x6dc740d2 = null
            0xc6f18fec = null
            0x87b8f3e2 = null
            0x1de0447d = null
            0x38c6c0ae = null
            0xc6145035 = null
            0xf500d365 = null
            0xecc2445d = null
            0xd0f89eed = null
            0x06d51709 = null
            0xd7c23dbd = null
            0x39dbef9e = null
            0x2cf5a52c = null
            0x57515a47 = null
            0x22d12f9f = null
            0x34e0ebc3 = null
            0x16372994 = null
            0x5bb0f73a = null
            0x1fcd9b0d = null
            0xd96126f4 = null
            0x781cfce6 = null
            0x1cab8909 = null
            0x59a8caf6 = null
            0x17e6b6c2 = null
            0xdbe38656 = null
            0xee4d3496 = null
            0x5347c307 = null
            0x9ee2888c = null
            0x17a1a151 = null
            0xb6beb28a = null
            0x74e7405a = null
            0xaef471f0 = null
            0x72e59f67 = null
            0x94951a84 = null
            0xc930ee6c = null
            0x7bd6890d = null
            0xbb42673e = null
            0xa1c6020e = null
            0x87edee67 = null
            0xc912d7cd = null
            0x43f55e27 = null
            0x826ca080 = null
            0xb30ea4a2 = null
            0x44a4ffac = null
            0x140ef17d = null
            0x9c5f2c26 = null
            0x48c9c0d7 = null
            0xe07bf76c = null
            0x68aebc46 = null
            0x66616f4b = null
            0x519a86c6 = null
            0x954c617a = null
            0xc5eef00e = null
            0xf8177c41 = null
            0xdbdcf0b4 = null
            0x2c908866 = null
            0x0a45175a = null
            0x25624a73 = null
            0x8d76ba2c = null
            0xca2f0847 = null
            0xfff796d5 = null
            0x399f1c45 = null
            0x5e2bd6f8 = null
            0x93d079c5 = null
            0xc24a9782 = null
            0x90d8d142 = null
            0x3285f24c = null
            0x13160753 = null
            0x66b0378b = null
            0x26ebe58a = null
            0xb58c225c = null
            0xcaddbe9f = null
            0x07ec5489 = null
            0xf4077d0b = null
            0x58ada8cf = null
            0x1c055875 = null
            0x80aab86e = null
            0xfc0ffc7a = null
            0x5888fc52 = null
            0x0d584327 = null
            0x791463b6 = null
            0xf2bf8e13 = null
            0xc23412ff = null
            0xd2430d2a = null
            0x551d1e9e = null
            0xf2724f8d = null
            0x0afa0573 = null
            0xb51be10c = null
            0xf7742e34 = null
            0x98249bf2 = null
            0x62626809 = null
            0x162e59c2 = null
            0x87d1939a = MapGroup {
                members: list2[string] = {
                    "24f70617-3890-4d47-a7c5-dd13f102bcd8"
                    "73744f69-e6b6-4c59-9899-170fa3b58a1e"
                }
                transform: mtx44 = {
                    -0.999999523, 0, 2.38418551e-07, 0
                    0, 1, 0, 0
                    -2.38418551e-07, 0, -0.999999523, 0
                    1009.45764, 136.666626, 2720.69995, 1
                }
                name: string = "group3"
            }
            0xac821b5e = null
            0xc9c71e54 = null
            0xc4b4250b = null
            0x401ddfa1 = null
            0x2796299c = null
            0x42911f36 = null
            0x3d17ef87 = null
            0xf9db0e40 = null
            0xdc7b58b0 = null
            0x81e54b8d = null
            0x41934d92 = null
            0x36b07081 = null
            0x8eb4917e = null
            0x1ffca1fd = null
            0x2bf2365f = null
            0xcdde7826 = null
            0x29e82a87 = null
            0x796d2707 = null
            0x145aae8c = null
            0xc190a344 = null
            0xac453af7 = null
            0xc23ee4e7 = null
            0x40e512fe = null
            0x9ebc624f = null
            0x6e66ebb6 = null
            0x9400b9b7 = null
            0x9f5e3c98 = null
            0x0d4f2db1 = null
            0x4790794f = null
            0x43f48220 = null
            0x0bc4ed1e = null
            0xe70f9a1a = null
            0x9213a4f5 = null
            0x099bd012 = null
            0xe9f1533e = null
            0x58d4474d = null
            0x29f528b0 = null
            0x0f4731cb = null
            0x29eea516 = null
            0xb7971511 = null
            0x03c3e6db = null
            0xef8b63b2 = null
            0x150036c7 = null
            0x6a40ce98 = null
            0x5b18b966 = null
            0x173a65a5 = null
            0xe6e57258 = null
            0x3385d815 = null
            0xf18e1d85 = null
            0x16848946 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x53c15a9e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 950.559814, 185.223526, 2651.823 }
                boxMax: vec3 = { 1021.02734, 234.593903, 2722.29077 }
                extraInfo: list[pointer] = {
                    GDSMapObjectAnimationInfo {
                        defaultAnimation: string = "idle1"
                    }
                }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.274249792, 0, -0.961658657, 0
                    0, 1, 0, 0
                    0.961658657, 0, -0.274249792, 0
                    985.793579, 184.135818, 2687.05688, 1
                }
                name: string = "LevelProp_TFT_BoardPoro"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdf91013f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Frostguard" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x4beb30ec = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.22754, 258.248535, 984.008789, 1
                }
                name: string = "TFT_Freljord_Wind2"
            }
            0x5be18a80 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000.6051, -474.026672, 2213.05249, 1
                }
                name: string = "TFT_Freljord_Godrays2"
            }
            0xd44f6171 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Snow"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1577.9303, 69.9951706, 1930.54834, 1
                }
                name: string = "TFT_Freljord_Snow2"
            }
            0xab607683 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1025.29004, 260.322754, 931.105164, 1
                }
                name: string = "TFT_BrazierFire_E1"
            }
            0xefd7b38e = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.30933, 260.754791, 927.898376, 1
                }
                name: string = "TFT_BrazierFire_E2"
            }
            0xe074635c = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1030.19604, 260.322754, 3028.86646, 1
                }
                name: string = "TFT_BrazierFire_E3"
            }
            0x0afe28ad = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2978.41382, 260.322754, 3026.11841, 1
                }
                name: string = "TFT_BrazierFire_E4"
            }
            0xf68fda1c = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1983.84705, 96.8508606, 250, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Fog1"
            }
            0x3b5bbfd3 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1976.58606, -289.149139, 232, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Fog2"
            }
            0xa7f503aa = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.22754, 258.248535, 3118.60376, 1
                }
                name: string = "TFT_Freljord_Wind1"
            }
            0xd9c2d312 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2948.59448, 268.860962, 919.382324, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Edge_Fog1"
            }
            0x980b1368 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1004.42517, 268.860962, 919.382324, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Edge_Fog2"
            }
            0xa596933b = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    598.352417, 595.616028, 2157.12817, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Edge_Fog3"
            }
            0x99b53310 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3345.16748, 623.045715, 2174.51196, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Edge_Fog4"
            }
            0xd584d67d = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_FrostGuard_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2060.41113, 196.25238, 3176.55884, 1
                }
                name: string = "TFT_Freljord_FrostGuard_Edge_Fog5"
            }
            0x120ae4c3 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard_Muted"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3679.69507, -401.230103, 2177.88306, 1
                }
                name: string = "TFT_BrazierFire_E5"
            }
            0x73c692f2 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_FrostGuard_Muted"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    409.255859, -401.230133, 2168.52734, 1
                }
                name: string = "TFT_BrazierFire_E6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Frostguard"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Frostguard" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xd2bbd2f9 = MapLightingVolume {
                sunColor: vec4 = { 0.419607848, 0.411764711, 0.490196079, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                skyLightColor: vec4 = { 0.227450982, 0.215686277, 0.521568656, 1 }
                horizonColor: vec4 = { 0.631372571, 0.815686285, 1, 1 }
                groundColor: vec4 = { 0.490196079, 0.423529416, 0.56078434, 1 }
                skyLightScale: f32 = 0.649999976
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.0509803928, 0.219607845, 0.819607854, 1 }
                fogAlternateColor: vec4 = { 0.372549027, 0.549019635, 0.917647064, 1 }
                fogStartAndEnd: vec2 = { 350, -800 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2032.48315, -927.355957, 2193.8706, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Frostguard"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2912.56494, 3, 2291.08301, 1
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
                    1110.23596, 0, 1693.47803, 1
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
                    2791.72803, 0, 2892.43091, 1
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
                    3050.87988, 0, 2846.68994, 1
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
                    928.268982, 0, 1132.08398, 1
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
                    -0.99999994, 8.74227766e-08, 0, 0
                    8.74227695e-08, 0.999999881, 8.74227766e-08, 0
                    7.64274186e-15, 8.74227695e-08, -0.99999994, 0
                    2067, 0, 2394, 1
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
                    1142.53601, 0, 1411.255, 1
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
                    2863.53394, 0, 2627.49097, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base"
    }
    "Maps/MapGeometry/Map22/Freljord_Frostguard" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Freljord_Frostguard"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.43921569, 0.203921571, 0.396078438, 1 }
                sunDirection: vec3 = { -0.384805739, 0.827142715, -0.409584463 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.301960796, 0.152941182, 0.368627459, 1 }
                horizonColor: vec4 = { 0.223529413, 0.192156866, 0.388235301, 1 }
                groundColor: vec4 = { 0.145098045, 0.160784319, 0.286274523, 1 }
                skyLightScale: f32 = 0.100000001
                lightMapColorScale: f32 = 2.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.333333343, 0, 0.498039216, 1 }
                fogAlternateColor: vec4 = { 0.333333343, 0.333333343, 0.498039216, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.20000005
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Freljord_Frostguard/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.800000012
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Frostguard_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0xfff6d589 = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared"
            0x2645b6b4 = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Frostguard"
            0x593cf3bc = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Frostguard"
            0x9379554e = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Frostguard"
            0xd6eb635f = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Frostguard"
            0x8048fd86 = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Frostguard"
            "Skybox_Freljord" = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
            "LevelProps_Shared" = "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared"
            "Freljord_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base"
        }
    }
}
