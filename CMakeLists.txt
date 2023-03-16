cmake_minimum_required(VERSION 3.10.0)
project(cmake_wrapper)

if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
  include(conanbuildinfo.cmake)
endif()
conan_basic_setup()

include(CheckCSourceCompiles)
set(LIBM_TEST_SOURCE "#include<math.h>\nfloat f; int main(){sqrt(f);return 0;}")
check_c_source_compiles("${LIBM_TEST_SOURCE}" HAVE_MATH)
if(HAVE_MATH)
  set(LIBM_LIBRARIES)
else()
  set(CMAKE_REQUIRED_LIBRARIES m)
  check_c_source_compiles("${LIBM_TEST_SOURCE}" HAVE_LIBM_MATH)
  unset(CMAKE_REQUIRED_LIBRARIES)
  if(NOT HAVE_LIBM_MATH)
    message(FATAL_ERROR "Unable to use C math library functions")
  endif()
  set(LIBM_LIBRARIES m)
endif()

set(PACKAGE_VERSION 1.04)
set(INCHI_API_SOURCES
  source_subfolder/INCHI_API/inchi_dll/ichi_bns.c
  source_subfolder/INCHI_API/inchi_dll/ichi_io.c
  source_subfolder/INCHI_API/inchi_dll/ichican2.c
  source_subfolder/INCHI_API/inchi_dll/ichicano.c
  source_subfolder/INCHI_API/inchi_dll/ichicans.c
  source_subfolder/INCHI_API/inchi_dll/ichiisot.c
  source_subfolder/INCHI_API/inchi_dll/ichilnct.c
  source_subfolder/INCHI_API/inchi_dll/ichimak2.c
  source_subfolder/INCHI_API/inchi_dll/ichimake.c
  source_subfolder/INCHI_API/inchi_dll/ichimap1.c
  source_subfolder/INCHI_API/inchi_dll/ichimap2.c
  source_subfolder/INCHI_API/inchi_dll/ichimap4.c
  source_subfolder/INCHI_API/inchi_dll/ichinorm.c
  source_subfolder/INCHI_API/inchi_dll/ichiparm.c
  source_subfolder/INCHI_API/inchi_dll/ichiprt1.c
  source_subfolder/INCHI_API/inchi_dll/ichiprt2.c
  source_subfolder/INCHI_API/inchi_dll/ichiprt3.c
  source_subfolder/INCHI_API/inchi_dll/ichiqueu.c
  source_subfolder/INCHI_API/inchi_dll/ichiread.c
  source_subfolder/INCHI_API/inchi_dll/ichiring.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr1.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr2.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr3.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr4.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr5.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr6.c
  source_subfolder/INCHI_API/inchi_dll/ichirvr7.c
  source_subfolder/INCHI_API/inchi_dll/ichisort.c
  source_subfolder/INCHI_API/inchi_dll/ichister.c
  source_subfolder/INCHI_API/inchi_dll/ichitaut.c
  source_subfolder/INCHI_API/inchi_dll/ikey_base26.c
  source_subfolder/INCHI_API/inchi_dll/ikey_dll.c
  source_subfolder/INCHI_API/inchi_dll/inchi_dll.c
  source_subfolder/INCHI_API/inchi_dll/inchi_dll_a.c
  source_subfolder/INCHI_API/inchi_dll/inchi_dll_a2.c
  source_subfolder/INCHI_API/inchi_dll/inchi_dll_main.c
  source_subfolder/INCHI_API/inchi_dll/runichi.c
  source_subfolder/INCHI_API/inchi_dll/sha2.c
  source_subfolder/INCHI_API/inchi_dll/strutil.c
  source_subfolder/INCHI_API/inchi_dll/util.c
)

set(INCHI_API_HEADERS
  source_subfolder/INCHI_API/inchi_dll/aux2atom.h
  source_subfolder/INCHI_API/inchi_dll/extr_ct.h
  source_subfolder/INCHI_API/inchi_dll/ichi.h
  source_subfolder/INCHI_API/inchi_dll/ichi_bns.h
  source_subfolder/INCHI_API/inchi_dll/ichi_io.h
  source_subfolder/INCHI_API/inchi_dll/ichicano.h
  source_subfolder/INCHI_API/inchi_dll/ichicant.h
  source_subfolder/INCHI_API/inchi_dll/ichicomn.h
  source_subfolder/INCHI_API/inchi_dll/ichicomp.h
  source_subfolder/INCHI_API/inchi_dll/ichidrp.h
  source_subfolder/INCHI_API/inchi_dll/ichierr.h
  source_subfolder/INCHI_API/inchi_dll/ichimain.h
  source_subfolder/INCHI_API/inchi_dll/ichimake.h
  source_subfolder/INCHI_API/inchi_dll/ichinorm.h
  source_subfolder/INCHI_API/inchi_dll/ichiparm.h
  source_subfolder/INCHI_API/inchi_dll/ichiring.h
  source_subfolder/INCHI_API/inchi_dll/ichirvrs.h
  source_subfolder/INCHI_API/inchi_dll/ichisize.h
  source_subfolder/INCHI_API/inchi_dll/ichister.h
  source_subfolder/INCHI_API/inchi_dll/ichitaut.h
  source_subfolder/INCHI_API/inchi_dll/ichitime.h
  source_subfolder/INCHI_API/inchi_dll/ikey_base26.h
  source_subfolder/INCHI_API/inchi_dll/inchi_api.h
  source_subfolder/INCHI_API/inchi_dll/inchi_dll_a.h
  source_subfolder/INCHI_API/inchi_dll/inchi_dll_main.h
  source_subfolder/INCHI_API/inchi_dll/inchicmp.h
  source_subfolder/INCHI_API/inchi_dll/incomdef.h
  source_subfolder/INCHI_API/inchi_dll/inpdef.h
  source_subfolder/INCHI_API/inchi_dll/lreadmol.h
  source_subfolder/INCHI_API/inchi_dll/mode.h
  source_subfolder/INCHI_API/inchi_dll/sha2.h
  source_subfolder/INCHI_API/inchi_dll/strutil.h
  source_subfolder/INCHI_API/inchi_dll/util.h
)
if(WIN32)
  set(INCHI_API_DLL
    # source_subfolder/INCHI_API/vc9/inchi_dll/vc9_libinchi.def
    source_subfolder/INCHI_API/vc9/inchi_dll/INCHI_DLL.rc
  )
endif()

if(INCHI_BUILD_SHARED)
  add_library(inchi SHARED ${INCHI_API_SOURCES} ${INCHI_API_HEADERS} ${INCHI_API_DLL})
  target_compile_definitions(inchi PRIVATE _USRDLL)
  target_compile_definitions(inchi PUBLIC BUILD_LINK_AS_DLL)
else()
  add_library(inchi STATIC ${INCHI_API_SOURCES} ${INCHI_API_HEADERS})
endif()

target_include_directories(inchi PRIVATE source_subfolder/INCHI_API/inchi_dll/)

set_target_properties(inchi PROPERTIES PUBLIC_HEADER source_subfolder/INCHI_API/inchi_dll/inchi_api.h)
target_link_libraries(inchi PUBLIC ${LIBM_LIBRARIES})

include(GNUInstallDirs)
install(TARGETS inchi
        EXPORT InchiTargets
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
                COMPONENT Inchi_Runtime
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
                COMPONENT Inchi_Runtime
                NAMELINK_COMPONENT Inchi_Development
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
                COMPONENT Inchi_Development
        INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
                COMPONENT Inchi_Development
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
                COMPONENT Inchi_Development
        )

set(INCHI_MAIN_SOURCES
  source_subfolder/INCHI_API/inchi_main/e_0dstereo.c
  source_subfolder/INCHI_API/inchi_main/e_ichi_io.c
  source_subfolder/INCHI_API/inchi_main/e_ichi_parms.c
  source_subfolder/INCHI_API/inchi_main/e_ichimain.c
  source_subfolder/INCHI_API/inchi_main/e_ichimain_a.c
  source_subfolder/INCHI_API/inchi_main/e_inchi_atom.c
  source_subfolder/INCHI_API/inchi_main/e_mol2atom.c
  source_subfolder/INCHI_API/inchi_main/e_readinch.c
  source_subfolder/INCHI_API/inchi_main/e_readmol.c
  source_subfolder/INCHI_API/inchi_main/e_readstru.c
  source_subfolder/INCHI_API/inchi_main/e_util.c
)

set(INCHI_MAIN_HEADERS
  source_subfolder/INCHI_API/inchi_main/e_0dstereo.h
  source_subfolder/INCHI_API/inchi_main/e_comdef.h
  source_subfolder/INCHI_API/inchi_main/e_ctl_data.h
  source_subfolder/INCHI_API/inchi_main/e_ichi_io.h
  source_subfolder/INCHI_API/inchi_main/e_ichi_parms.h
  source_subfolder/INCHI_API/inchi_main/e_ichicomp.h
  source_subfolder/INCHI_API/inchi_main/e_ichierr.h
  source_subfolder/INCHI_API/inchi_main/e_ichisize.h
  source_subfolder/INCHI_API/inchi_main/e_inchi_atom.h
  source_subfolder/INCHI_API/inchi_main/e_inpdef.h
  source_subfolder/INCHI_API/inchi_main/e_mode.h
  source_subfolder/INCHI_API/inchi_main/e_readmol.h
  source_subfolder/INCHI_API/inchi_main/e_readstru.h
  source_subfolder/INCHI_API/inchi_main/e_util.h
  source_subfolder/INCHI_API/inchi_main/ichitime.h
  source_subfolder/INCHI_API/inchi_main/inchi_api.h
  source_subfolder/INCHI_API/inchi_main/lreadmol.h
)
if(WIN32)
  set(INCHI_MAIN_RES
    source_subfolder/INCHI_API/vc9/inchi_main/resource.h
    source_subfolder/INCHI_API/vc9/inchi_main/inchi_main1.rc
  )
endif()

add_executable(inchi_main ${INCHI_MAIN_SOURCES} ${INCHI_MAIN_HEADERS} ${INCHI_MAIN_RES})
target_link_libraries(inchi_main PUBLIC inchi ${LIBM_LIBRARIES})
set_target_properties(inchi_main PROPERTIES OUTPUT_NAME "inchi")

target_include_directories(inchi_main PRIVATE source_subfolder/INCHI_API/inchi_dll/)
target_include_directories(inchi_main PRIVATE source_subfolder/INCHI_API/inchi_main/)

install(TARGETS inchi_main
        EXPORT InchiTargets
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
                COMPONENT Inchi_Runtime
        )
