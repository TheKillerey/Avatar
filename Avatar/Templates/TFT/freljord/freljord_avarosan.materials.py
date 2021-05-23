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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Grass_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Grass_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Grass_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/Tree_Bend_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/Tree_Bend_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Trees_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_Avarosa_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_Avarosa_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_B.TFT_Freljord.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_B_Mask.TFT_Freljord.dds"
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
                value: vec4 = { 0.121568628, 0.525490224, 0.568627477, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Bounds"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Frequency"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Speed"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { 0.75, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Frequency"
                value: vec4 = { 6, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Glow_Opacity"
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_SmoothStep"
                value: vec4 = { 0.25, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity_Min_Max"
                value: vec4 = { 0.200000003, 1, 0, 0 }
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
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_UV_SCROLL_GLOW"
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
                on: bool = false
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
        dynamicMaterial: pointer = DynamicMaterialDef {}
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
    "Maps/Particles/TFT/Base/TFT_BrazierFire_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                emitterName: string = "Fire"
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
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbook_01.SRI_Slots.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_mult.SRI_Slots.dds"
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
                emitterName: string = "sparks"
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
                texDiv: vec2 = { 2, 2 }
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
                emitterName: string = "Smoke"
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "baseGlow1"
                blendMode: u8 = 4
                pass: i16 = 50
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
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
                pass: i16 = 80
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "mouth_flame_R3"
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
                        constantValue: vec3 = { 0, 30, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                pass: i16 = -2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 3.0999999 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 60, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
        }
        particleName: string = "TFT_BrazierFire_A"
        particlePath: string = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
        flags: u8 = 197
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3500
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_owl_hoot"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Wind" = VfxSystemDefinitionData {
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
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 200, 0, 200 }
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
                                { 200, 0, 200 }
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
                    constantValue: vec4 = { 1, 0.76000613, 0.420004576, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.76000613, 0.420004576, 0 }
                            { 1, 0.76000613, 0.420004576, 0.800000012 }
                            { 1, 0.76000613, 0.420004576, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
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
                    constantValue: vec2 = { -0.25, 0.25 }
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
                            { -0.25, 0.25 }
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
                    constantValue: vec2 = { -0.0500000007, 0.0500000007 }
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
                            { -0.0500000007, 0.0500000007 }
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
        particleName: string = "TFT_Freljord_Avarosa_Wind"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Wind"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Fog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                    constantValue: vec4 = { 1, 0.862745106, 0.360784322, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.862745106, 0.360784322, 0 }
                            { 1, 0.862745106, 0.360784322, 1 }
                            { 1, 0.862745106, 0.360784322, 0 }
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
                emitterName: string = "WindDark"
                disabled: bool = true
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
                blendMode: u8 = 1
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
                    constantValue: vec4 = { 1, 0.859998465, 0.360006094, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.859998465, 0.360006094, 0 }
                            { 1, 0.859998465, 0.360006094, 0.500007629 }
                            { 1, 0.859998465, 0.360006094, 0 }
                        }
                    }
                }
                pass: i16 = 49
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
        }
        visibilityRadius: f32 = 8000
        particleName: string = "TFT_Freljord_Avarosa_Fog"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Fog"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3500
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_wind_tree_gust"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Godrays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Godray"
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
                    constantValue: vec4 = { 1, 0.850003839, 0.330006868, 0.650003791 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 0.850003839, 0.330006868, 0.650003791 }
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
                            { 1, 0.549019635, 0.250980407, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_GodRays.TFT_Freljord.dds"
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
        particleName: string = "TFT_Freljord_Avarosa_Godrays"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Godrays"
        flags: u8 = 132
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Fire"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_fire_bright_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3500
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_wind_cold_gust"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_insects_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_insects_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_insects_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_insects_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Air_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Air_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Air_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_air_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Snow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                constantValue: f32 = 10
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "Snow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, -100, 100 }
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
                            { 100, -100, 100 }
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
                    constantValue: vec4 = { 1, 0.78039217, 0.423529416, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.78039217, 0.423529416, 0 }
                            { 1, 0.78039217, 0.423529416, 0.600000024 }
                            { 1, 0.78039217, 0.423529416, 0 }
                        }
                    }
                }
                pass: i16 = 100
                isDirectionOriented: flag = true
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 10, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Firefly_Mote.TFT_Set5.dds"
                uvMode: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                constantValue: f32 = 10
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 20
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "Snow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, -100, 100 }
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
                            { 100, -100, 100 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Avarosa_Leaves_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
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
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.400000006 }
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
                            { 0.666666985, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                    constantValue: vec3 = { 1.79999995, 1.79999995, 1.79999995 }
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
                            { 1.79999995, 1.79999995, 1.79999995 }
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
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Avarosa_Leaves_2x2.TFT_Freljord.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Freljord_Avarosa_Snow"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Snow"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3500
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_elk_cry"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Bird_Call" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 3500
        particleName: string = "TFT_Audio-Emitter_Freljord_Avarosan_Bird_Call"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Bird_Call"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_avarosan_bird_call"
    }
    0x1db70ad9 = MapPointLightType {
        lightColor: vec4 = { 0, 0.427450985, 0.611764729, 1 }
        radius: f32 = 519
        castStaticShadows: bool = false
    }
    0x2e2d5df2 = MapPointLightType {
        lightColor: vec4 = { 0, 0.407843143, 0.392156869, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xafadfc34 = MapPointLightType {
        lightColor: vec4 = { 1, 0.58431375, 0, 1 }
        radius: f32 = 941
        Impact: i32 = 1
    }
    0xf232d9bd = MapPointLightType {
        lightColor: vec4 = { 0.749019623, 0.549019635, 0.443137258, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xf449b3ec = MapPointLightType {
        lightColor: vec4 = { 0.988235295, 0.266666681, 0, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
    0xd14201ac = MapPointLightType {
        lightColor: vec4 = { 0.0274509825, 0.36470589, 0.870588303, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Avarosan" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x5c643e0a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Air_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1907.74988, -11.8725281, 2135.41308, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Air_Loop1"
            }
            0x239903fe = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_insects_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2055.62549, 20.5325928, 2036.03833, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_insects_Loop1"
            }
            0x5b99b04c = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3409.48291, 0, 2031.70996, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry1"
            }
            0xbfcbe3a6 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    395.160034, 386.887207, 2189.19726, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot1"
            }
            0x0ffac850 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3420.11865, 17.6171265, 2055.26172, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust1"
            }
            0xc7e8887a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    444.272339, -227.895325, 2213.93799, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust1"
            }
            0x6228627c = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3222.44531, -129.745361, 1511.71655, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Tree_Gust2"
            }
            0xcbb30aa1 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    583.415894, -26.3144531, 2643.45581, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Wind_Cold_Gust2"
            }
            0x38dd42ff = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.39404, 290, 3024.06201, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Fire1"
            }
            0x1a9abfed = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1026.15295, 290, 3014.70898, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Fire2"
            }
            0x05b98b41 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1028.43604, 290, 928.234009, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Fire3"
            }
            0x0b58aa92 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2975.79004, 290, 929.187988, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Fire4"
            }
            0xd4f0a03a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3537.1206, 0, 3215.77734, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Owl_Hoot2"
            }
            0x29a25f49 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    429.154663, -1890.91699, 1758.96631, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Elk_Cry2"
            }
            0xda47f36a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_Avarosan_Bird_Call"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1222.40625, 0, 2040.59717, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_Avarosan_Bird_Call1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Avarosan"
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
    "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Avarosan" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x9ca478ab = MapLightingVolume {
                sunColor: vec4 = { 0.749019623, 0.674509823, 0.607843161, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                skyLightColor: vec4 = { 0.729411781, 0.68235296, 0.56078434, 1 }
                horizonColor: vec4 = { 0.776470602, 0.87843138, 0.31764707, 1 }
                groundColor: vec4 = { 0.325490206, 0.431372553, 0.56078434, 1 }
                skyLightScale: f32 = 0.699999988
                lightMapColorScale: f32 = 1.89999998
                fogColor: vec4 = { 0.349019617, 0.623529434, 0.80392158, 1 }
                fogAlternateColor: vec4 = { 0.196078435, 0.337254912, 0.4627451, 1 }
                fogStartAndEnd: vec2 = { 750, -900 }
                transform: mtx44 = {
                    2703.2561, 0, 0, 0
                    0, 4113.65039, 0, 0
                    0, 0, 2938.32178, 0
                    2032.48315, -983.576172, 2193.8706, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Avarosan"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdf91013f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Avarosan" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xb4db3855 = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749999583
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2973.50293, 446.985962, 3020.83301, 1
                }
                name: string = "Light_Orange5"
            }
            0x3430be28 = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749999702
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1029.45056, 446.985962, 3023.55566, 1
                }
                name: string = "Light_Orange6"
            }
            0x4b37bff0 = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749999166
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2973.81445, 446.985962, 935.325073, 1
                }
                name: string = "Light_Orange7"
            }
            0xcb6c5826 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749998689
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    243.455505, -397.79834, 1121.95996, 1
                }
                name: string = "light_48_13"
            }
            0x82d4d42f = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749999404
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1026.55835, 446.985962, 937.80542, 1
                }
                name: string = "Light_Orange8"
            }
            0xd45add15 = MapPointLight {
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
            0x2307da6b = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749998033
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3675.61157, -294.125824, 2174.98975, 1
                }
                name: string = "Light_Orange1"
            }
            0xd366f16a = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.749997556
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    410.431671, -238.913177, 2174.80078, 1
                }
                name: string = "Light_Orange2"
            }
            0x74cff5a6 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1109.802, 334, 1445.56604, 1
                }
                name: string = "light_40_2"
            }
            0xdb0ad80f = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.7169649
                intensityScale: f32 = 1.60000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1568.42578, 467.099487, 2280.74219, 1
                }
                name: string = "light_40_1"
            }
            0x578df832 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2910.31421, 344.789581, 2522.34253, 1
                }
                name: string = "light_40_4"
            }
            0xbc7c8d19 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.399999917
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3380.32397, 369.65271, 1518.86133, 1
                }
                name: string = "light_40_3"
            }
            0xc32226de = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.399999917
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2293.99146, 267.725464, 3031.27271, 1
                }
                name: string = "light_40_7"
            }
            0xf3438b6e = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.399999917
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2582.20435, 267.725464, 932.828735, 1
                }
                name: string = "light_40_8"
            }
            0x8a1b26a4 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.74999851
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    97.8235779, -325.401825, 3173.03808, 1
                }
                name: string = "light_48_1"
            }
            0x2fb6d3c8 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749996364
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3731.39453, 295.891083, 3037.94019, 1
                }
                name: string = "light_48_2"
            }
            0xda1074eb = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749997914
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    851.321777, -325.401825, 3815.57593, 1
                }
                name: string = "light_48_3"
            }
            0xb5748ca7 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.749999762
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3078.76538, 727.834229, 3709.53589, 1
                }
                name: string = "light_40_9"
            }
            0x3ef2b752 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749995589
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4208.92432, -653.678467, 1906.44238, 1
                }
                name: string = "light_48_4"
            }
            0xb8710972 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749994814
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3741.2312, -313.506989, 785.520508, 1
                }
                name: string = "light_48_5"
            }
            0x4764cabe = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749994338
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2909.84863, -429.596954, 316.352661, 1
                }
                name: string = "light_48_6"
            }
            0x8692cc34 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.74999404
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    992.577271, -429.596954, 218.393066, 1
                }
                name: string = "light_48_7"
            }
            0xac27ff35 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749999285
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -122.98645, -584.942261, 1929.86108, 1
                }
                name: string = "light_48_8"
            }
            0xa1c38add = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 1.49999988
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.70605, 66.5248184, 441.105011, 1
                }
                name: string = "light_61_1"
            }
            0x6cf1a32e = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 1.15760612
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3295.74072, -195.949112, 2127.55322, 1
                }
                name: string = "light_61_2"
            }
            0xa9d08b20 = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 1.15760612
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    669.588501, -195.949112, 2184.56836, 1
                }
                name: string = "light_61_3"
            }
            0x33cb1508 = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 1.25
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3209.11157, 227.970734, 428.223541, 1
                }
                name: string = "light_61_4"
            }
            0x3d665271 = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3525.19507, 247.930527, 2785.06299, 1
                }
                name: string = "light_61_6"
            }
            0xe143dddf = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3585.95874, 247.930527, 1265.84094, 1
                }
                name: string = "light_61_7"
            }
            0xd0aead70 = MapPointLight {
                type: link = 0x1db70ad9
                radiusScale: f32 = 1.49999797
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    796.177002, 227.970734, 222.170929, 1
                }
                name: string = "light_61_8"
            }
            0x755f0fd7 = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.716964602
                intensityScale: f32 = 1.60000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2465.3457, 467.099487, 2280.74219, 1
                }
                name: string = "light_40_10"
            }
            0x2384d412 = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.716964602
                intensityScale: f32 = 1.60000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2465.3457, 526.145325, 1585.84509, 1
                }
                name: string = "light_40_11"
            }
            0x5550ed3f = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 0.716964602
                intensityScale: f32 = 1.60000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1568.42578, 467.099487, 1585.84509, 1
                }
                name: string = "light_40_12"
            }
            0x2b3245c1 = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.273987502
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    816.684021, 338.964386, 1274.26917, 1
                }
                name: string = "Light_Orange3"
            }
            0xefa31cf6 = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749998629
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    345.376923, -470.36441, 1906.63232, 1
                }
                name: string = "light_48_9"
            }
            0x6f13d57b = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.749995112
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3778.05225, -494.974182, 1959.01465, 1
                }
                name: string = "light_48_10"
            }
            0x69fa51dc = MapPointLight {
                type: link = 0x2e2d5df2
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2042.90552, 622.887451, 2014.18066, 1
                }
                name: string = "light_48_11"
            }
            0xcf7f6ac8 = MapPointLight {
                type: link = 0xafadfc34
                radiusScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1851.51758, 325.503632, 3295.94019, 1
                }
                name: string = "light_40_5"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Avarosan"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Avarosan" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe83c111b = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Snow"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1999.52783, 69.9951706, 1930.54834, 1
                }
                name: string = "TFT_Freljord_Snow2"
            }
            0x29d51a7b = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.22754, 258.248535, 1936.88049, 1
                }
                name: string = "TFT_Freljord_Wind2"
            }
            0x23c6e7e3 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000.6051, -129.80484, 1928.62354, 1
                }
                name: string = "TFT_Freljord_Godrays2"
            }
            0x1f9dc05b = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1025.67163, 252.352142, 929.2052, 1
                }
                name: string = "TFT_BrazierFire_A1"
            }
            0x8e75acf1 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2976.33789, 252.10199, 928.333618, 1
                }
                name: string = "TFT_BrazierFire_A2"
            }
            0x24c9b183 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1027.05615, 253.08429, 3025.3479, 1
                }
                name: string = "TFT_BrazierFire_A3"
            }
            0xb59ac909 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.00708, 251.550598, 3024.36182, 1
                }
                name: string = "TFT_BrazierFire_A4"
            }
            0x6ea38a92 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1983, 239, 250, 1
                }
                name: string = "TFT_Freljord_Avarosa_Fog1"
            }
            0x821780a4 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_Avarosa_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1976, -147, 232, 1
                }
                name: string = "TFT_Freljord_Avarosa_Fog2"
            }
            0xdbe22754 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3678.67285, -410.070435, 2179.35425, 1
                }
                name: string = "TFT_BrazierFire_A5"
            }
            0x2c051b29 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    409.902283, -408.60022, 2172.53931, 1
                }
                name: string = "TFT_BrazierFire_A6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Avarosan"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Avarosan" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x6c3be0f7 = null
            0x169a043f = null
            0x2dd02b64 = null
            0x35dd39fd = null
            0xd817ed18 = null
            0xbe689914 = null
            0xc6d0797c = null
            0x3f786d55 = null
            0x89543a38 = null
            0xe9ac4078 = null
            0x7ac070cd = null
            0xf9a6f61c = null
            0x570db03c = null
            0xf45bfa76 = null
            0x560b3136 = null
            0x388407bd = null
            0x79923001 = null
            0xdf424beb = null
            0x366234a6 = null
            0x783bcbf3 = null
            0x22fb62e1 = null
            0x4c44e6c8 = null
            0x07a07d4a = null
            0xede35eb0 = null
            0xbd3c284f = null
            0xe8a3d98f = null
            0x0981694a = null
            0x2e4e2ab1 = null
            0xac512859 = null
            0xa597aaa9 = null
            0x833d8743 = null
            0x7d4fcef9 = null
            0x235f3578 = null
            0x891c1a99 = null
            0x946d7a08 = null
            0x7323f07e = null
            0xbb2f91aa = null
            0x2db0d808 = null
            0x70035947 = null
            0xf7115f86 = null
            0x30023c05 = null
            0x64dd80d4 = null
            0xabcd20e6 = null
            0xd5118291 = null
            0x93d18ef1 = null
            0x93c74ce7 = null
            0x997f320c = null
            0xa417a433 = null
            0x7378cb67 = null
            0xb393a945 = null
            0x33f71539 = null
            0x3fc2d056 = null
            0x2c661dca = null
            0x05e70072 = null
            0x14b9c1c8 = null
            0xab193e06 = null
            0xf5d817b1 = null
            0x29291185 = null
            0x6ddcb5f5 = null
            0x509c09fa = null
            0x56ebb4f8 = null
            0x00b748c8 = null
            0xf6b8d140 = null
            0x2f71354a = null
            0xd956f457 = null
            0xf657baab = null
            0x77a64ea0 = null
            0x1be88fff = null
            0xc4efbe72 = null
            0x739a9e0f = null
            0xd0313aab = null
            0x40b1f5de = null
            0x638daaa2 = null
            0x1801bb66 = null
            0x34fc72ac = null
            0x3fac9b62 = null
            0xd8adbc0c = null
            0x945e27e5 = null
            0xeca4cc69 = null
            0xa3d25cc9 = null
            0x6ea1f853 = null
            0xe50d5dba = null
            0x5e716641 = null
            0x5f6cd3c2 = null
            0xa7928699 = null
            0x0223ff3d = null
            0xd854772c = null
            0x884e2b0e = null
            0x215ada3a = null
            0x41402b94 = null
            0xf00d1a3d = null
            0xe04eba04 = null
            0x7d31f279 = null
            0x3e7f4e1d = null
            0x437def4e = null
            0xeedc0035 = null
            0x3bca07fd = null
            0xea5afeba = null
            0x9f219d96 = null
            0x0fbf8a52 = null
            0xbbd7b67f = null
            0xd3fa2941 = null
            0x79618868 = null
            0xba17daf6 = null
            0xdc1acb44 = null
            0x5a5dd2e1 = null
            0x0732434f = null
            0x222fe855 = null
            0xaa0967c5 = null
            0x5c354b1f = null
            0xeb2d896a = null
            0xd93765ae = null
            0x298ca067 = null
            0x431bd983 = null
            0x3f7eee2f = null
            0x178a9c2d = null
            0x54f51f96 = null
            0x4d97fdfb = null
            0x308ce45a = null
            0x6b7ed9d8 = null
            0x20ea41e1 = null
            0x8df279cd = null
            0xf69eb169 = null
            0x1e5bff04 = null
            0x5fb3d0c9 = null
            0x62d08e4d = null
            0x717fbe18 = null
            0x96c0d4d2 = null
            0x03f6024f = null
            0x3536bfba = null
            0xa64b646c = null
            0xa16ccaa7 = null
            0xe7c7d9aa = null
            0x5ebfa5ea = null
            0x40db1fb4 = null
            0xd7cdeab3 = null
            0x5ab062e3 = null
            0x33c29841 = null
            0x5a6a1cbe = null
            0x31059a15 = null
            0x3982dda0 = null
            0x39d8897d = null
            0xff6e7b6f = null
            0xf362859b = null
            0xa192600b = null
            0x82ab28c4 = null
            0x5c904971 = null
            0x40bbe20e = null
            0x66310056 = null
            0x2236e514 = null
            0xe2bb0079 = null
            0x404249f0 = null
            0xeb6642f0 = null
            0x5a5da54c = null
            0xabea7bb7 = null
            0x74d19f9a = null
            0xbbf2651c = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Avarosan"
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
    "Maps/MapGeometry/Map22/Freljord_Avarosan" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Freljord_Avarosan"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.78039217, 0.482352942, 0.309803933, 1 }
                sunDirection: vec3 = { -0.384805739, 0.827142715, -0.409584463 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.854901969, 0.717647076, 0.301960796, 1 }
                horizonColor: vec4 = { 0.58431375, 0.58431375, 0.286274523, 1 }
                groundColor: vec4 = { 0.184313729, 0.392156869, 0.396078438, 1 }
                skyLightScale: f32 = 0.349999994
                lightMapColorScale: f32 = 2.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.0627451017, 0.0549019612, 0.109803922, 1 }
                fogAlternateColor: vec4 = { 0.376470596, 0.392156869, 0.419607848, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 0.850000024
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Freljord_Avarosan/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.800000012
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Avarosan_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0xfff6d589 = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared"
            0x10188bbe = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_Avarosan"
            0x9c3f2876 = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_Avarosan"
            0xf465fff4 = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_Avarosan"
            0x26088ec9 = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Avarosan"
            0xb4b8c55c = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_Avarosan"
            "Skybox_Freljord" = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
            "LevelProps_Shared" = "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared"
            "Freljord_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base"
        }
    }
}
