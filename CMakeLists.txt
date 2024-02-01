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

set(PACKAGE_VERSION 1.07-beta3)
add_compile_definitions(TARGET_API_LIB)
set(INCHI_API_SOURCES
  source_subfolder/INCHI_API/libinchi/src/ichilnct.c
  source_subfolder/INCHI_API/libinchi/src/inchi_dll.c
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_a.c
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_a2.c
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_b.c
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_main.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_builder.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_inchikey_builder.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_mol.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_read_inchi.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_read_mol.c
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_status.c
  source_subfolder/INCHI_BASE/src/ichican2.c
  source_subfolder/INCHI_BASE/src/ichicano.c
  source_subfolder/INCHI_BASE/src/ichicans.c
  source_subfolder/INCHI_BASE/src/ichierr.c
  source_subfolder/INCHI_BASE/src/ichiisot.c
  source_subfolder/INCHI_BASE/src/ichimak2.c
  source_subfolder/INCHI_BASE/src/ichimake.c
  source_subfolder/INCHI_BASE/src/ichimap1.c
  source_subfolder/INCHI_BASE/src/ichimap2.c
  source_subfolder/INCHI_BASE/src/ichimap4.c
  source_subfolder/INCHI_BASE/src/ichinorm.c
  source_subfolder/INCHI_BASE/src/ichiparm.c
  source_subfolder/INCHI_BASE/src/ichiprt1.c
  source_subfolder/INCHI_BASE/src/ichiprt2.c
  source_subfolder/INCHI_BASE/src/ichiprt3.c
  source_subfolder/INCHI_BASE/src/ichiqueu.c
  source_subfolder/INCHI_BASE/src/ichiread.c
  source_subfolder/INCHI_BASE/src/ichiring.c
  source_subfolder/INCHI_BASE/src/ichirvr1.c
  source_subfolder/INCHI_BASE/src/ichirvr2.c
  source_subfolder/INCHI_BASE/src/ichirvr3.c
  source_subfolder/INCHI_BASE/src/ichirvr4.c
  source_subfolder/INCHI_BASE/src/ichirvr5.c
  source_subfolder/INCHI_BASE/src/ichirvr6.c
  source_subfolder/INCHI_BASE/src/ichirvr7.c
  source_subfolder/INCHI_BASE/src/ichisort.c
  source_subfolder/INCHI_BASE/src/ichister.c
  source_subfolder/INCHI_BASE/src/ichitaut.c
  source_subfolder/INCHI_BASE/src/ichi_bns.c
  source_subfolder/INCHI_BASE/src/ichi_io.c
  source_subfolder/INCHI_BASE/src/ikey_base26.c
  source_subfolder/INCHI_BASE/src/ikey_dll.c
  source_subfolder/INCHI_BASE/src/inchi_gui.c
  source_subfolder/INCHI_BASE/src/mol2atom.c
  source_subfolder/INCHI_BASE/src/mol_fmt1.c
  source_subfolder/INCHI_BASE/src/mol_fmt2.c
  source_subfolder/INCHI_BASE/src/mol_fmt3.c
  source_subfolder/INCHI_BASE/src/mol_fmt4.c
  source_subfolder/INCHI_BASE/src/readinch.c
  source_subfolder/INCHI_BASE/src/runichi.c
  source_subfolder/INCHI_BASE/src/runichi2.c
  source_subfolder/INCHI_BASE/src/runichi3.c
  source_subfolder/INCHI_BASE/src/runichi4.c
  source_subfolder/INCHI_BASE/src/sha2.c
  source_subfolder/INCHI_BASE/src/strutil.c
  source_subfolder/INCHI_BASE/src/util.c
)

set(INCHI_API_HEADERS
  source_subfolder/INCHI_API/libinchi/src/inchi_dll.h
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_a.h
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_b.h
  source_subfolder/INCHI_API/libinchi/src/inchi_dll_main.h
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_mol.h
  source_subfolder/INCHI_API/libinchi/src/ixa/ixa_status.h
  source_subfolder/INCHI_API/libinchi/vc14/resource.h
  source_subfolder/INCHI_API/tbb/scalable_allocator.h
  source_subfolder/INCHI_API/tbb/tbbmalloc_proxy_for_inchi.h
  source_subfolder/INCHI_BASE/src/aux2atom.h
  source_subfolder/INCHI_BASE/src/extr_ct.h
  source_subfolder/INCHI_BASE/src/ichi.h
  source_subfolder/INCHI_BASE/src/ichicano.h
  source_subfolder/INCHI_BASE/src/ichicant.h
  source_subfolder/INCHI_BASE/src/ichicomn.h
  source_subfolder/INCHI_BASE/src/ichicomp.h
  source_subfolder/INCHI_BASE/src/ichidrp.h
  source_subfolder/INCHI_BASE/src/ichierr.h
  source_subfolder/INCHI_BASE/src/ichimain.h
  source_subfolder/INCHI_BASE/src/ichimake.h
  source_subfolder/INCHI_BASE/src/ichinorm.h
  source_subfolder/INCHI_BASE/src/ichiring.h
  source_subfolder/INCHI_BASE/src/ichirvrs.h
  source_subfolder/INCHI_BASE/src/ichisize.h
  source_subfolder/INCHI_BASE/src/ichister.h
  source_subfolder/INCHI_BASE/src/ichitaut.h
  source_subfolder/INCHI_BASE/src/ichitime.h
  source_subfolder/INCHI_BASE/src/ichi_bns.h
  source_subfolder/INCHI_BASE/src/ichi_io.h
  source_subfolder/INCHI_BASE/src/ikey_base26.h
  source_subfolder/INCHI_BASE/src/inchicmp.h
  source_subfolder/INCHI_BASE/src/inchi_api.h
  source_subfolder/INCHI_BASE/src/inchi_gui.h
  source_subfolder/INCHI_BASE/src/incomdef.h
  source_subfolder/INCHI_BASE/src/inpdef.h
  source_subfolder/INCHI_BASE/src/ixa.h
  source_subfolder/INCHI_BASE/src/mode.h
  source_subfolder/INCHI_BASE/src/mol_fmt.h
  source_subfolder/INCHI_BASE/src/readinch.h
  source_subfolder/INCHI_BASE/src/sha2.h
  source_subfolder/INCHI_BASE/src/strutil.h
  source_subfolder/INCHI_BASE/src/tbb/tbbmalloc_proxy.h
  source_subfolder/INCHI_BASE/src/util.h
)
if(WIN32)
  set(INCHI_API_DLL
    source_subfolder/INCHI_API/vc14/libinchi.rc
  )
endif()

if(INCHI_BUILD_SHARED)
  add_library(inchi SHARED ${INCHI_API_SOURCES} ${INCHI_API_HEADERS} ${INCHI_API_DLL})
  target_compile_definitions(inchi PRIVATE _USRDLL)
  target_compile_definitions(inchi PUBLIC BUILD_LINK_AS_DLL)
else()
  add_library(inchi STATIC ${INCHI_API_SOURCES} ${INCHI_API_HEADERS})
endif()

target_include_directories(inchi PRIVATE source_subfolder/INCHI_API/libinchi/src/)

set_target_properties(inchi PROPERTIES PUBLIC_HEADER source_subfolder/INCHI_BASE/src/inchi_api.h)
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
  source_subfolder/INCHI_API/demos/inchi_main/src/e_0dstereo.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichimain.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichimain_a.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichi_io.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichi_parms.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_inchi_atom.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_mol2atom.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_readinch.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_readmol.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_readstru.c
  source_subfolder/INCHI_API/demos/inchi_main/src/e_util.c
  source_subfolder/INCHI_EXE/inchi-1/src/dispstru.c
  source_subfolder/INCHI_EXE/inchi-1/src/ichimain.c
)

set(INCHI_MAIN_HEADERS
  source_subfolder/INCHI_API/demos/inchi_main/src/aux2atom.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_0dstereo.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_comdef.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ctl_data.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichicomp.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichierr.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichisize.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichitime.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_ichi_io.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_inchi_atom.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_inpdef.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_main.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_mode.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_mol_frmt.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_readmol.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_readstru.h
  source_subfolder/INCHI_API/demos/inchi_main/src/e_util.h
  source_subfolder/INCHI_API/demos/inchi_main/vc14/resource.h
)
if(WIN32)
  set(INCHI_MAIN_RES
    source_subfolder/INCHI_API/demos/inchi_main/vc14/resource.h
    source_subfolder/INCHI_API/demos/inchi_main/vc14/inchi_main.rc
  )
endif()

add_executable(inchi_main ${INCHI_MAIN_SOURCES} ${INCHI_MAIN_HEADERS} ${INCHI_MAIN_RES})
target_link_libraries(inchi_main PUBLIC inchi ${LIBM_LIBRARIES})
set_target_properties(inchi_main PROPERTIES OUTPUT_NAME "inchi")

target_include_directories(inchi_main PRIVATE source_subfolder/INCHI_API/libinchi/src/)
target_include_directories(inchi_main PRIVATE source_subfolder/INCHI_BASE/src/)

install(TARGETS inchi_main
        EXPORT InchiTargets
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
                COMPONENT Inchi_Runtime
        )
