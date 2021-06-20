"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Texture_Name"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Noise_Texture"
                textureName: string = "ASSETS/Shared/Materials/SRX_FireTest.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Tint_Color"
                value: vec4 = { 0.0799999982, -0.0599999987, -0.0599999987, 0.349999994 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "DISABLE_FIRE_FX"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "MASK_FX_IN_MAP_CENTER"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            NOBAKEDLIGHTINGTEMP
            DISABLEDEPTHFOG
            PREMULTIPLIEDALPHA
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/SRX_Blend_Infernal_Ground"
                        cullEnable: bool = false
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "env_transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "ENV_TRANSITION" = "1"
                }
            }
        }
    }