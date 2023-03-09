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

set(PACKAGE_VERSION 1.06)

# source locations
set(INCHI_BASE_SRC source_subfolder/INCHI_BASE/src)
set(LIB_INCHI_SRC source_subfolder/INCHI_API/libinchi/src)
set(LIB_INCHI_IXA source_subfolder/INCHI_API/libinchi/src/ixa)
set(INCHI_TBB source_subfolder/INCHI_API/tbb)
set(INCHI_DEMOS source_subfolder/INCHI_API/demos/inchi_main/src)
set(LIB_VC source_subfolder/INCHI_API/libinchi/vc14)
set(MAIN_VC source_subfolder/INCHI_API/demos/inchi_main/vc14)
set(INCHI_EXE source_subfolder/INCHI_EXE/inchi-1/src)

add_compile_definitions(TARGET_API_LIB)
set(INCHI_API_SOURCES
  ${LIB_INCHI_SRC}/ichilnct.c
  ${LIB_INCHI_SRC}/inchi_dll.c
  ${LIB_INCHI_SRC}/inchi_dll_a.c
  ${LIB_INCHI_SRC}/inchi_dll_a2.c
  ${LIB_INCHI_SRC}/inchi_dll_b.c
  ${LIB_INCHI_SRC}/inchi_dll_main.c
  ${LIB_INCHI_IXA}/ixa_builder.c
  ${LIB_INCHI_IXA}/ixa_inchikey_builder.c
  ${LIB_INCHI_IXA}/ixa_mol.c
  ${LIB_INCHI_IXA}/ixa_read_inchi.c
  ${LIB_INCHI_IXA}/ixa_read_mol.c
  ${LIB_INCHI_IXA}/ixa_status.c
  ${INCHI_BASE_SRC}/ichican2.c
  ${INCHI_BASE_SRC}/ichicano.c
  ${INCHI_BASE_SRC}/ichicans.c
  ${INCHI_BASE_SRC}/ichierr.c
  ${INCHI_BASE_SRC}/ichiisot.c
  ${INCHI_BASE_SRC}/ichimak2.c
  ${INCHI_BASE_SRC}/ichimake.c
  ${INCHI_BASE_SRC}/ichimap1.c
  ${INCHI_BASE_SRC}/ichimap2.c
  ${INCHI_BASE_SRC}/ichimap4.c
  ${INCHI_BASE_SRC}/ichinorm.c
  ${INCHI_BASE_SRC}/ichiparm.c
  ${INCHI_BASE_SRC}/ichiprt1.c
  ${INCHI_BASE_SRC}/ichiprt2.c
  ${INCHI_BASE_SRC}/ichiprt3.c
  ${INCHI_BASE_SRC}/ichiqueu.c
  ${INCHI_BASE_SRC}/ichiread.c
  ${INCHI_BASE_SRC}/ichiring.c
  ${INCHI_BASE_SRC}/ichirvr1.c
  ${INCHI_BASE_SRC}/ichirvr2.c
  ${INCHI_BASE_SRC}/ichirvr3.c
  ${INCHI_BASE_SRC}/ichirvr4.c
  ${INCHI_BASE_SRC}/ichirvr5.c
  ${INCHI_BASE_SRC}/ichirvr6.c
  ${INCHI_BASE_SRC}/ichirvr7.c
  ${INCHI_BASE_SRC}/ichisort.c
  ${INCHI_BASE_SRC}/ichister.c
  ${INCHI_BASE_SRC}/ichitaut.c
  ${INCHI_BASE_SRC}/ichi_bns.c
  ${INCHI_BASE_SRC}/ichi_io.c
  ${INCHI_BASE_SRC}/ikey_base26.c
  ${INCHI_BASE_SRC}/ikey_dll.c
  ${INCHI_BASE_SRC}/inchi_gui.c
  ${INCHI_BASE_SRC}/mol2atom.c
  ${INCHI_BASE_SRC}/mol_fmt1.c
  ${INCHI_BASE_SRC}/mol_fmt2.c
  ${INCHI_BASE_SRC}/mol_fmt3.c
  ${INCHI_BASE_SRC}/mol_fmt4.c
  ${INCHI_BASE_SRC}/readinch.c
  ${INCHI_BASE_SRC}/runichi.c
  ${INCHI_BASE_SRC}/runichi2.c
  ${INCHI_BASE_SRC}/runichi3.c
  ${INCHI_BASE_SRC}/runichi4.c
  ${INCHI_BASE_SRC}/sha2.c
  ${INCHI_BASE_SRC}/strutil.c
  ${INCHI_BASE_SRC}/util.c
)

set(INCHI_API_HEADERS
  ${LIB_INCHI_SRC}/inchi_dll.h
  ${LIB_INCHI_SRC}/inchi_dll_a.h
  ${LIB_INCHI_SRC}/inchi_dll_b.h
  ${LIB_INCHI_SRC}/inchi_dll_main.h
  ${LIB_INCHI_IXA}/ixa_mol.h
  ${LIB_INCHI_IXA}/ixa_status.h
  ${LIB_VC}/resource.h
  ${INCHI_TBB}/scalable_allocator.h
  ${INCHI_TBB}/tbbmalloc_proxy_for_inchi.h
  ${INCHI_BASE_SRC}/aux2atom.h
  ${INCHI_BASE_SRC}/extr_ct.h
  ${INCHI_BASE_SRC}/ichi.h
  ${INCHI_BASE_SRC}/ichicano.h
  ${INCHI_BASE_SRC}/ichicant.h
  ${INCHI_BASE_SRC}/ichicomn.h
  ${INCHI_BASE_SRC}/ichicomp.h
  ${INCHI_BASE_SRC}/ichidrp.h
  ${INCHI_BASE_SRC}/ichierr.h
  ${INCHI_BASE_SRC}/ichimain.h
  ${INCHI_BASE_SRC}/ichimake.h
  ${INCHI_BASE_SRC}/ichinorm.h
  ${INCHI_BASE_SRC}/ichiring.h
  ${INCHI_BASE_SRC}/ichirvrs.h
  ${INCHI_BASE_SRC}/ichisize.h
  ${INCHI_BASE_SRC}/ichister.h
  ${INCHI_BASE_SRC}/ichitaut.h
  ${INCHI_BASE_SRC}/ichitime.h
  ${INCHI_BASE_SRC}/ichi_bns.h
  ${INCHI_BASE_SRC}/ichi_io.h
  ${INCHI_BASE_SRC}/ikey_base26.h
  ${INCHI_BASE_SRC}/inchicmp.h
  ${INCHI_BASE_SRC}/inchi_api.h
  ${INCHI_BASE_SRC}/inchi_gui.h
  ${INCHI_BASE_SRC}/incomdef.h
  ${INCHI_BASE_SRC}/inpdef.h
  ${INCHI_BASE_SRC}/ixa.h
  ${INCHI_BASE_SRC}/mode.h
  ${INCHI_BASE_SRC}/mol_fmt.h
  ${INCHI_BASE_SRC}/readinch.h
  ${INCHI_BASE_SRC}/sha2.h
  ${INCHI_BASE_SRC}/strutil.h
  ${INCHI_BASE_SRC}/tbb/tbbmalloc_proxy.h
  ${INCHI_BASE_SRC}/util.h
)
if(WIN32)
  set(INCHI_API_DLL
    ${LIB_VC}/libinchi.rc
  )
endif()

if(INCHI_BUILD_SHARED)
  add_library(inchi SHARED ${INCHI_API_SOURCES} ${INCHI_API_HEADERS} ${INCHI_API_DLL})
  target_compile_definitions(inchi PRIVATE _USRDLL)
  target_compile_definitions(inchi PUBLIC BUILD_LINK_AS_DLL)
else()
  add_library(inchi STATIC ${INCHI_API_SOURCES} ${INCHI_API_HEADERS})
endif()

target_include_directories(inchi PRIVATE ${LIB_INCHI_SRC})

set_target_properties(inchi PROPERTIES PUBLIC_HEADER ${INCHI_BASE_SRC}/inchi_api.h)
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
  ${INCHI_DEMOS}/e_0dstereo.c
  ${INCHI_DEMOS}/e_ichimain.c
  ${INCHI_DEMOS}/e_ichimain_a.c
  ${INCHI_DEMOS}/e_ichi_io.c
  ${INCHI_DEMOS}/e_ichi_parms.c
  ${INCHI_DEMOS}/e_inchi_atom.c
  ${INCHI_DEMOS}/e_mol2atom.c
  ${INCHI_DEMOS}/e_readinch.c
  ${INCHI_DEMOS}/e_readmol.c
  ${INCHI_DEMOS}/e_readstru.c
  ${INCHI_DEMOS}/e_util.c
  ${INCHI_EXE}/dispstru.c
  ${INCHI_EXE}/ichimain.c
)

set(INCHI_MAIN_HEADERS
  ${INCHI_DEMOS}/aux2atom.h
  ${INCHI_DEMOS}/e_0dstereo.h
  ${INCHI_DEMOS}/e_comdef.h
  ${INCHI_DEMOS}/e_ctl_data.h
  ${INCHI_DEMOS}/e_ichicomp.h
  ${INCHI_DEMOS}/e_ichierr.h
  ${INCHI_DEMOS}/e_ichisize.h
  ${INCHI_DEMOS}/e_ichitime.h
  ${INCHI_DEMOS}/e_ichi_io.h
  ${INCHI_DEMOS}/e_inchi_atom.h
  ${INCHI_DEMOS}/e_inpdef.h
  ${INCHI_DEMOS}/e_main.h
  ${INCHI_DEMOS}/e_mode.h
  ${INCHI_DEMOS}/e_mol_frmt.h
  ${INCHI_DEMOS}/e_readmol.h
  ${INCHI_DEMOS}/e_readstru.h
  ${INCHI_DEMOS}/e_util.h
  ${MAIN_VC}/resource.h
)
if(WIN32)
  set(INCHI_MAIN_RES
    ${MAIN_VC}/resource.h
    ${MAIN_VC}/inchi_main.rc
  )
endif()

add_executable(inchi_main ${INCHI_MAIN_SOURCES} ${INCHI_MAIN_HEADERS} ${INCHI_MAIN_RES})
target_link_libraries(inchi_main PUBLIC inchi ${LIBM_LIBRARIES})
set_target_properties(inchi_main PROPERTIES OUTPUT_NAME "inchi")

target_include_directories(inchi_main PRIVATE ${LIB_INCHI_SRC})
target_include_directories(inchi_main PRIVATE ${INCHI_BASE_SRC})

install(TARGETS inchi_main
        EXPORT InchiTargets
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
                COMPONENT Inchi_Runtime
        )
