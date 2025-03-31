/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button as RadixThemesButton, Container as RadixThemesContainer, Flex as RadixThemesFlex, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Link as RadixThemesLink } from "@radix-ui/themes"
import { ColorModeContext, EventLoopContext } from "$/utils/context"
import { Event, isTrue } from "$/utils/state"
import { MoonIcon as LucideMoonIcon, SunIcon as LucideSunIcon } from "lucide-react"
import { Button } from "$/custom/button"
import NextLink from "next/link"
import NextHead from "next/head"



export function Fragment_6603094d9d8ace7144f9e046a6e3130d () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)





  
  return (
    <Fragment>

{(resolvedColorMode === "light") ? (
  <Fragment>

<LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
  )
}

export function Iconbutton_7db6525f1e338c54eb55df627d1421bc () {
  
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])



  
  return (
    <RadixThemesIconButton css={({ ["padding"] : "6px", ["position"] : "fixed", ["top"] : "2rem", ["right"] : "2rem", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) })} onClick={on_click_9922dd3e837b9e087c86a2522c2c93f8}>

<Fragment_6603094d9d8ace7144f9e046a6e3130d/>
</RadixThemesIconButton>
  )
}

export function Button_9adf8a9609be6ad31d7a1d055236a12a () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_05dd4fca7f8c0463c2ef2590c93b76be = useCallback(((_e) => (addEvents([(Event("reflex___state____state.reflex_experiment___reflex_experiment____state.handle_evt", ({ ["value"] : ({ ["ctrl_key"] : _e["ctrlKey"], ["alt_key"] : _e["altKey"], ["shift_key"] : _e["shiftKey"], ["meta_key"] : _e["metaKey"], ["client_x"] : _e["clientX"], ["client_y"] : _e["clientY"], ["screen_x"] : _e["screenX"], ["screen_y"] : _e["screenY"], ["pressure"] : _e["pressure"], ["pointer_type"] : _e["pointerType"], ["button"] : _e["button"], ["buttons"] : _e["buttons"], ["movement_x"] : _e["movementX"], ["movement_y"] : _e["movementY"], ["width"] : _e["width"], ["height"] : _e["height"], ["tilt_x"] : _e["tiltX"], ["tilt_y"] : _e["tiltY"], ["tangential_pressure"] : _e["tangentialPressure"], ["twist"] : _e["twist"], ["is_primary"] : _e["isPrimary"], ["pointer_id"] : _e["pointerId"], ["target"] : _e["target"], ["current_target"] : _e["currentTarget"], ["related_target"] : _e["relatedTarget"], ["time_stamp"] : _e["timeStamp"], ["type"] : _e["type"], ["bubbles"] : _e["bubbles"], ["cancelable"] : _e["cancelable"], ["default_prevented"] : _e["defaultPrevented"], ["composed"] : _e["composed"], ["is_trusted"] : _e["isTrusted"], ["event_phase"] : _e["eventPhase"], ["detail"] : _e["detail"], ["view"] : _e["view"], ["which"] : _e["which"], ["get_modifier_state"] : _e["getModifierState"], ["composed_path"] : _e["composedPath"], ["prevent_default"] : _e["preventDefault"], ["stop_immediate_propagation"] : _e["stopImmediatePropagation"], ["stop_propagation"] : _e["stopPropagation"] }) }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    <Button className={"bg-red-500"} onClick={on_click_05dd4fca7f8c0463c2ef2590c93b76be}>

{"Click me!"}
</Button>
  )
}

export function Link_e61c3d7cba79d2ee9269c3e7fdc2d6bf () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)





  
  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} size={"3"}>

<NextLink href={"https://reflex.dev"} passHref={true}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["textAlign"] : "center", ["padding"] : "1em" })} direction={"row"} gap={"3"}>

{"Built with "}
<svg aria-label={"Reflex"} css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} height={"12"} role={"img"} width={"56"} xmlns={"http://www.w3.org/2000/svg"}>

<path d={"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}/>
<path d={"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}/>
<path d={"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}/>
<path d={"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}/>
<path d={"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}/>
<path d={"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"}/>
<title>

{"Reflex"}
</title>
</svg>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<RadixThemesContainer css={({ ["padding"] : "16px" })} size={"3"}>

<Iconbutton_7db6525f1e338c54eb55df627d1421bc/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["minHeight"] : "85vh" })} direction={"column"} justify={"center"} gap={"5"}>

<RadixThemesHeading size={"9"}>

{"Welcome to Reflex!"}
</RadixThemesHeading>
<Button_9adf8a9609be6ad31d7a1d055236a12a/>
<RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} target={(true ? "_blank" : "")}>

<NextLink href={"https://reflex.dev/docs/getting-started/introduction/"} passHref={true}>

<RadixThemesButton>

{"Check out our docs!"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
</RadixThemesFlex>
<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })}>

<Link_e61c3d7cba79d2ee9269c3e7fdc2d6bf/>
</RadixThemesFlex>
</RadixThemesContainer>
<NextHead>

<title>

{"ReflexExperiment | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
